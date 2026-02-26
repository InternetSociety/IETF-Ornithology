#!/usr/bin/env python

import re
import os
import sys
import pprint
from pathlib import Path
import argparse
import requests
from requests.exceptions import HTTPError
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo


debug = 0


parser = argparse.ArgumentParser(
    prog="ApprovedBOFs",
    description="""
                    Lists the currently approved BOF requests in the IETF
                    This tool assumes a specif path.
                    """,
    epilog="""Tool specificly developed for the IETF  Ornmithology.
                                           """,
)

parser.add_argument("meetingnumber", help="IETF meeting number ")




args = parser.parse_args()
meetingnumber = args.meetingnumber

# Determine IETF meeting ID in Datatrakker
IETFMeetingId = None
datatrackerUrl = (
    "https://datatracker.ietf.org/api/v1/meeting/meeting/?format=json&number="
    + meetingnumber
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
        pprint.pprint (jsonResponse)
    IETFMeetingId = jsonResponse["objects"][0]["id"]
     # Potential bug: not sure about the first index in the object array
except HTTPError as http_err:
    print(
        f"HTTP error occured while processing  fetching {datatrackerUrl}: {http_err}"
    )
except Exception as err:
    print(
        f"Other error occured while processing fetching {datatrackerUrl}: {err}"
    )

if not IETFMeetingId:
    print ("Could not determine meeting date")
    exit(1)


bofIDs = []

datatrackerUrl = (
    "https://datatracker.ietf.org/api/v1/group/group/?state=bof&meeting=" + str(IETFMeetingId)
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
        pprint.pprint(jsonResponse)
    if (not jsonResponse["objects"]) :
        print ("No BOF groups found for meeting " + meetingnumber)
        exit(1)
    
    bofIDs = [obj["id"] for obj in jsonResponse["objects"] if "id" in obj]
       
    for obj in jsonResponse["objects"]:
        if "name" in obj:
            name = obj["name"]
        if "acronym" in obj:
            acronym = obj["acronym"]
        print("* [" + name + "(" + acronym + ")](./"+acronym+".md)")    
    print ("\n ---------\n"  )
    for obj in jsonResponse["objects"]:
        if "# name" in obj:
            name = obj["name"]
        if "acronym" in obj:
            acronym = obj["acronym"]
        try:
            with open("src/IETF/BOFs/"+acronym+".md", "x", encoding="utf-8") as f:
                f.write("# " + name + " (" + acronym + ")\n")  
                f.write("<IETFschedule meets=false></IETFschedule>\n")
                f.write("* [BoF request]( LOOK UP )\n")
                f.write("* Potentially of interest because: \n")
                f.write("* Keywords: ")
        except FileExistsError:
            print("File src/IETF/BOFs/"+acronym+".md already exists; not overwriting.")
        
    if debug:
        pprint.pprint(bofIDs)
except HTTPError as http_err:
    print(
        f"HTTP error occured while processing {meetingnumber} and fetching {datatrackerUrl}: {http_err}"
    )
except Exception as err:
    print(
        f"Other error occured while processing meeting {meetingnumber} and fetching {datatrackerUrl}: {err}"
    )
    
    
for bofID in bofIDs:
    datatrackerUrl = "https://datatracker.ietf.org/api/v1/meeting/session/?format=json&group=" + str(bofID) + "&meeting=" + str(IETFMeetingId)
    if debug:
        print(datatrackerUrl)
    try:
        response = requests.get(datatrackerUrl)
        response.raise_for_status()
        # access JSOn content
        jsonResponse = response.json()
        if debug:
            print("Entire JSON response")
            pprint.pprint(jsonResponse)
            
    except HTTPError as http_err:
        print(
            f"HTTP error occured while processing bofID {bofID} and fetching {datatrackerUrl}: {http_err}"
        )
    except Exception as err:
        print(
         f"Other error occured while processing bofID {bofID} and fetching {datatrackerUrl}: {err}"
        )

            