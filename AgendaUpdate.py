#!/usr/bin/env python

import re
from pathlib import Path
import argparse
import requests
from requests.exceptions import HTTPError
from datetime import datetime
from zoneinfo import ZoneInfo


debug = 0


parser = argparse.ArgumentParser(
    prog="AgendaUpdate",
    description="""
                    Updates the agenda information in the various files..
                    The tool expect the path to end with a filename that equals a working group acronym.
                    It will modify the  line with the matching <IETFschedule> XML elements
                    and fill in agenda details from the IETF datatracker. Note it will delete all data
                    in front of the XML tag too.
                    """,
    epilog="""Tool specificly developed for the IETF  Ornmithology.
                      For timezone names see  https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
                                           """,
)

parser.add_argument("meetingnumber", help="IETF meeting number ")
parser.add_argument("timezonename", help="For instance America/Vancouver")
parser.add_argument("--acronym", nargs="?", help="wg acroynm")
parser.add_argument("path")

args = parser.parse_args()
meetingnumber = args.meetingnumber
timezonename = args.timezonename
filepath = Path(args.path)
if not filepath.exists():
    print("Fie " + filepath.as_posix() + " does not exist")
    exit(1)

# Determine meeting acronym from filename
if args.acronym:
    acronym = args.acronym
else:
    acronym = filepath.stem
    if acronym == "intro":
        exit(1)

if debug:
    print(acronym.upper())


# Determine IETF meeting ID in Datatrakker
datatrackerUrl = (
    "https://datatracker.ietf.org/api/v1/meeting/meeting/?format=json&acronym=&number="
    + meetingnumber
)
IETFMeetingId = 0
if debug:
    print(datatrackerUrl)
try:
    response = requests.get(datatrackerUrl)
    response.raise_for_status()
    # access JSOn content
    jsonResponse = response.json()
    if debug:
        print("Entire JSON response")
        print(jsonResponse)
    IETFMeetingId = jsonResponse["objects"][0][
        "id"
    ]  # Potential bug: not sure about the first index in the object array
except HTTPError as http_err:
    print(
        f"HTTP error occured wile processing {acronym.upper()} and fetching {datatrackerUrl}: {http_err}"
    )
except Exception as err:
    print(
        f"Other error occured wile processing {acronym.upper()} and fetching {datatrackerUrl}: {err}"
    )

if not IETFMeetingId:
    exit(1)

if debug:
    print("IETFMeetingID:" + str(IETFMeetingId))


# Determine Workinggroup ID in Datatrakker
workgroupId = 0
datatrackerUrl = (
    "https://datatracker.ietf.org/api/v1/group/group/?format=json&acronym=" + acronym
)
if debug:
    print(datatrackerUrl)
try:
    response = requests.get(datatrackerUrl)
    response.raise_for_status()
    # access JSOn content
    jsonResponse = response.json()
    if debug:
        print("Entire JSON response")
        print(jsonResponse)
    if not jsonResponse["objects"]:
        print (acronym.upper() + " is not a known group" )
        exit(1)
    workgroupId = jsonResponse["objects"][0][
        "id"
    ]  # Potential bug: not sure about the first index in the object array

except HTTPError as http_err:
    print(
        f"HTTP error occured wile processing {acronym.upper()} and fetching {datatrackerUrl}: {http_err}"
    )
except Exception as err:
    print(
        f"Other error occured wile processing {acronym.upper()}  fetching {datatrackerUrl}: {err}"
    )

if not workgroupId:
    exit(1)

if debug:
    print("WorkingroupID:" + str(workgroupId))


# Find the sceduling entry
# First determine the sechduled time assignment
sessionID = ""
datatrackerUrl = (
    "https://datatracker.ietf.org/api/v1/meeting/session/?format=json&group="
    + str(workgroupId)
    + "&meeting="
    + str(IETFMeetingId)
)

if debug:
    print(datatrackerUrl)
try:
    response = requests.get(datatrackerUrl)
    response.raise_for_status()
    # access JSOn content
    jsonResponse = response.json()
    if debug:
        print("Entire JSON response")
        print(jsonResponse)
    if not jsonResponse["objects"]:
        print (acronym.upper() + " likely does not meet at IETF" + meetingnumber )
        exit(1)
    # workgroupId = jsonResponse["objects"][0]["id"]   # Potential bug: not sure about the first index in the object array
    sessionID = jsonResponse["objects"][0]["id"]
except HTTPError as http_err:
    print(
        f"HTTP error occured wile processing {acronym.upper()} and fetching {datatrackerUrl}: {http_err}"
    )
except Exception as err:
    print(
        f"Other error occured wile processing {acronym.upper()} and fetching {datatrackerUrl}: {err}"
    )

if sessionID == "":
    exit(1)

if debug:
    print("sessionId:" + str(sessionID))


# Determine the most recent
schedTimeAssignmentID = ""
datatrackerUrl = "https://datatracker.ietf.org/api/v1/meeting/schedtimesessassignment/?format=json&session=" + str(sessionID) + "&limit=30"
if debug:
    print(datatrackerUrl)
try:
    response = requests.get(datatrackerUrl)
    response.raise_for_status()
    # access JSOn content
    jsonResponse = response.json()
    if debug:
        print("Entire JSON response")
        print(jsonResponse)
    schedtimesessassignmentObjects=jsonResponse["objects"]


    lastModifiedTime=datetime.strptime(schedtimesessassignmentObjects[0]["modified"], "%Y-%m-%dT%H:%M:%S%z")
    schedTimeAssignmentID=schedtimesessassignmentObjects[0]["id"]
    i = 1
    while i < len(schedtimesessassignmentObjects):
        newModifiedTime = datetime.strptime(schedtimesessassignmentObjects[i]["modified"], "%Y-%m-%dT%H:%M:%S%z")
        if lastModifiedTime < newModifiedTime:
            lastModifiedTime = newModifiedTime
            schedTimeAssignmentID=schedtimesessassignmentObjects[i]["id"]
        i+=1
        if debug:
            print (str(i)+ " : " + lastModifiedTime.strftime("%a %d %b %Y %H:%M"))



except HTTPError as http_err:
    print(
        f"HTTP error occured wile processing {acronym.upper()} and fetching {datatrackerUrl}: {http_err}"
    )
except Exception as err:
    print(
        f"Other error occured wile processing {acronym.upper()} and fetching {datatrackerUrl}: {err}"
    )



# Get the timeSlotURL
timeSlotURL = ""
datatrackerUrl = "https://datatracker.ietf.org/api/v1/meeting/schedtimesessassignment/" + str(schedTimeAssignmentID) + "/?format=json"
if debug:
    print(datatrackerUrl)
try:
    response = requests.get(datatrackerUrl)
    response.raise_for_status()
    # access JSOn content
    jsonResponse = response.json()
    if debug:
        print("Entire JSON response")
        print(jsonResponse)
    timeSlotURL = jsonResponse["timeslot"]

except HTTPError as http_err:
    print(
        f"HTTP error occured wile processing {acronym.upper()} and fetching {datatrackerUrl}: {http_err}"
    )
except Exception as err:
    print(
        f"Other error occured wile processing {acronym.upper()} and fetching {datatrackerUrl}: {err}"
    )

if timeSlotURL == "":
    exit(1)

if debug:
    print("timeSlotURL:" + str(timeSlotURL))

# parse the timeSlotURL
locationURL = ""
datatrackerUrl = "https://datatracker.ietf.org" + timeSlotURL + "?format=json"
if debug:
    print(datatrackerUrl)
try:
    response = requests.get(datatrackerUrl)
    response.raise_for_status()
    # access JSOn content
    jsonResponse = response.json()
    if debug:
        print("Entire JSON response")
        print(jsonResponse)
    locationURL = jsonResponse["location"]
    meetingtime = jsonResponse["time"]


except HTTPError as http_err:
    print(
        f"HTTP error occured wile processing {acronym.upper()} and fetching {datatrackerUrl}: {http_err}"
    )
except Exception as err:
    print(
        f"Other error occured wile processing {acronym.upper()} and  fetching {datatrackerUrl}: {err}"
    )

if locationURL == "":
    exit(1)
if not meetingtime:
    exit(1)


meetingtime_struct = datetime.strptime(meetingtime, "%Y-%m-%dT%H:%M:%S%z")
localmeetingtime_struct = meetingtime_struct.astimezone(ZoneInfo(timezonename))
if debug:
    print(localmeetingtime_struct.strftime("%a %d %b %Y %H:%M"))

datatrackerUrl = "https://datatracker.ietf.org" + locationURL + "?format=json"
if debug:
    print(datatrackerUrl)
try:
    response = requests.get(datatrackerUrl)
    response.raise_for_status()
    # access JSOn content
    jsonResponse = response.json()
    if debug:
        print("Entire JSON response")
        print(jsonResponse)
    roomname = jsonResponse["name"]
    functionalname = jsonResponse["functional_name"]

except HTTPError as http_err:
    print(
        f"HTTP error occured wile processing {acronym.upper()} and fetching {datatrackerUrl}: {http_err}"
    )
except Exception as err:
    print(
        f"Other error occured wile  processing {acronym.upper()} and fetching {datatrackerUrl}: {err}"
    )
if debug:
    print("Roomname: " + roomname + "(" + functionalname + ")")

# Now we arrived here we can parse our data

print(
    acronym.upper()
    + " @ "
    + meetingnumber
    + ": "
    + localmeetingtime_struct.strftime("%a %d %b %Y %H:%M")
    + " - "
    + roomname
)
# Read in the file / these are relatively small files we can do this in memory
with open(filepath, "r") as file:
    filedata = file.read()

# Write the file out again
with open(filepath, "w") as file:
    file.write(
        re.sub(
            ".*<IETFschedule>.*</IETFschedule>",
            "* <IETFschedule>IETF"
            + meetingnumber
            + ": "
            + localmeetingtime_struct.strftime("%a %d %b %Y %H:%M")
            + " - "
            + roomname
            + "</IETFschedule>",
            filedata,
        )
    )
