import re
import sys

# Get meeting number and filename from command line arguments
if len(sys.argv) < 3:
    print("Usage: python extract_groups.py <meeting_number> <filename>")
    sys.exit(1)

meeting_num = sys.argv[1]
filename = sys.argv[2]

# Read the file and extract groups matching pattern "GROUP @ meeting_num"
with open(filename, 'r') as f:
    content = f.read()

# Find all groups that match the pattern "GROUPNAME @ meeting_num:"
groups = re.findall(rf'^(\w+)\s+@\s+{meeting_num}:', content, re.MULTILINE)

# Convert to lowercase
groups_lowercase = [group.lower() for group in groups]

# Generate webcal and https URLs
groups_param = ','.join(groups_lowercase)

webcal_url = f"webcal://datatracker.ietf.org/meeting/{meeting_num}/agenda.ics?show={groups_param}"
ics_url = f"https://datatracker.ietf.org/meeting/{meeting_num}/agenda.ics?show={groups_param}"
https_url = f"https://datatracker.ietf.org/meeting/{meeting_num}/agenda?filters={groups_param}"



print(f"\n### Agenda\n You view the [datatrakcker page]({https_url}) with all groups mentioned that meet during IETFl{meeting_num}.")
print (f"\n\n You can subscribe to the calendar with the following using a [webcal]({webcal_url}) or an [ics]({ics_url}) link.\n")


