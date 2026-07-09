import re
import sys
from datetime import datetime
from pathlib import Path
import json
from urllib import parse, request

# Get meeting number and filename from command line arguments
if len(sys.argv) < 3:
    print("Usage: python create_agendaURL.py <meeting_number> <filename>")
    sys.exit(1)

meeting_num = sys.argv[1]
filename = sys.argv[2]

# Read the file and extract rows matching "GROUP @ meeting_num: TIME - ROOM"
with open(filename, 'r') as f:
    content = f.read()

# Capture group name, meeting time, and room from each matching line
rows = re.findall(
    rf'^([A-Za-z0-9-]+)\s+@\s+{meeting_num}:\s+(.+?)\s+-\s+(.+?)\s*$',
    content,
    re.MULTILINE,
)

groups = [group for group, _, _ in rows]


def parse_meeting_time(value):
    return datetime.strptime(value, "%a %d %b %Y %H:%M")


rows = sorted(rows, key=lambda row: parse_meeting_time(row[1]))


def build_group_file_map():
    src_dir = Path(__file__).resolve().parent / "src"
    group_files = {}

    if not src_dir.exists():
        return group_files

    for md_file in src_dir.rglob("*.md"):
        name = md_file.name.lower()
        if name.endswith(".bak"):
            continue

        stem = md_file.stem.lower()
        if stem in {"agenda", "summary", "introduction", "readme", "intro"}:
            continue

        if stem not in group_files:
            relative = md_file.relative_to(src_dir).as_posix()
            group_files[stem] = f"./{relative}"

    return group_files


def fetch_group_expansions(group_acronyms):
    expansions = {}

    for acronym in sorted(set(group_acronyms)):
        encoded = parse.quote(acronym)
        url = f"https://datatracker.ietf.org/api/v1/group/group/?format=json&acronym={encoded}"

        try:
            with request.urlopen(url, timeout=5) as response:
                data = json.load(response)
        except Exception:
            continue

        objects = data.get("objects", [])
        if not objects:
            continue

        name = objects[0].get("name", "").strip()
        if name:
            expansions[acronym] = name

    return expansions


group_file_map = build_group_file_map()
groups_lowercase = [group.lower() for group in groups]
group_expansions = fetch_group_expansions(groups_lowercase)

# Generate webcal and https URLs
groups_param = ','.join(groups_lowercase)

webcal_url = f"webcal://datatracker.ietf.org/meeting/{meeting_num}/agenda.ics?show={groups_param}"
ics_url = f"https://datatracker.ietf.org/meeting/{meeting_num}/agenda.ics?show={groups_param}"
https_url = f"https://datatracker.ietf.org/meeting/{meeting_num}/agenda?filters={groups_param}"



print(f"\n### Agenda\n You view the [datatrakcker page]({https_url}) with all groups mentioned in this document and that meet during IETFl{meeting_num}.")
print (f"\n\n You can subscribe to the calendar with the following using a [webcal]({webcal_url}) or an [ics]({ics_url}) link.\n")
print (f"Note that times in the calendar, and in this document are subject to change.")
print ("## Quick Glance\n")
if rows:
    print("\n\n|  Time | Room | Group |")
    print("|---|---|---|")
    for group, meeting_time, room in rows:
        group_link = group_file_map.get(group.lower())
        group_expansion = group_expansions.get(group.lower(), "").replace("|", "\\|")
        if group_expansion:
            display_name = f"{group} [{group_expansion}]"
        else:
            display_name = group

        group_cell = f"[{display_name}]({group_link})" if group_link else display_name
        print(f"| {meeting_time} | {room} | {group_cell} |")

