#!/usr/bin/env python

import re
import os
from pathlib import Path
import argparse
import requests
from requests.exceptions import HTTPError
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo


debug = 0


parser = argparse.ArgumentParser(
    prog="AgendaUpdate",
    description="""
                    Lists the working groups in the IETF that have seen a recent, i.e. younger than age of change, charter change.
                    This tool assumes a specif path.
                    """,
    epilog="""Tool specificly developed for the IETF  Ornmithology.
                                           """,
)

parser.add_argument("meetingnumber", help="IETF meeting number ")




args = parser.parse_args()
meetingnumber = args.meetingnumber

# Determine IETF meeting ID in Datatrakker
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
        print(jsonResponse)
    meetingDate = datetime.strptime(
           jsonResponse["objects"][0]["date"],"%Y-%m-%d"
        )

     # Potential bug: not sure about the first index in the object array
except HTTPError as http_err:
    print(
        f"HTTP error occured while processing  fetching {datatrackerUrl}: {http_err}"
    )
except Exception as err:
    print(
        f"Other error occured while processing fetching {datatrackerUrl}: {err}"
    )

if not meetingDate:
    print ("Could not determine meeting date")
    exit(1)



# Determine all active groups in IETF
# https://datatracker.ietf.org/api/v1/group/group/?format=json&state=active&type=wg
datatrackerUrl = "https://datatracker.ietf.org/api/v1/group/group/?format=json&state=active&type=wg&limit=250"

if debug:
    print(datatrackerUrl)
try:
    response = requests.get(datatrackerUrl)
    response.raise_for_status()
    # access JSOn content
    jsonResponse = response.json()
    if debug > 1:
        print("Entire JSON response")
        print(jsonResponse)

    ActiveGroups = jsonResponse[
        "objects"
    ]  # Potential bug: not sure about the first index in the object array
except HTTPError as http_err:
    print(f"HTTP error occured while fetching {datatrackerUrl}: {http_err}")
except Exception as err:
    print(f"Other error occured while fetching {datatrackerUrl}: {err}")

for group in ActiveGroups:
    acronym = group["acronym"]
    WGname = group["name"]
    datatrackerUrl = "https://datatracker.ietf.org" + group["charter"] + "/?format=json"
    if debug:
        print(datatrackerUrl)
    try:
        response = requests.get(datatrackerUrl)
        response.raise_for_status()
        # access JSOn content
        jsonResponse = response.json()
        if debug > 1:
            print("Entire JSON response")
            print(jsonResponse)

        LastChange = datetime.strptime(
            jsonResponse["time"], "%Y-%m-%dT%H:%M:%S%z"
        )  # Potential bug: not sure about the first index in the object array
        CharterName = jsonResponse["name"]

        CharterRev = jsonResponse["rev"]
        if CharterRev != "01":
            next
    except HTTPError as http_err:
        print(
            f"HTTP error occured while processing {acronym.upper()} and fetching {datatrackerUrl}: {http_err}"
        )
    except Exception as err:
        print(
            f"Other error occured while processing {acronym.upper()} and fetching {datatrackerUrl}: {err}"
        )
    if debug:
        print(LastChange)

 
    meetingDate = meetingDate.astimezone(ZoneInfo("UTC"))

    if meetingDate < LastChange:
        datatrackerUrl = (
            "https://datatracker.ietf.org" + group["parent"] + "?format=json"
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

            ParentArea = jsonResponse["acronym"]
        except HTTPError as http_err:
            print(
                f"HTTP error occured while processing {acronym.upper()} and fetching {datatrackerUrl}: {http_err}"
            )
        except Exception as err:
            print(
                f"Other error occured while processing {acronym.upper()} and fetching {datatrackerUrl}: {err}"
            )
        FilePath = ParentArea.upper() + "/" + acronym + ".md"



        if os.path.isfile("./src/IETF/" + FilePath):
            print(
                " * "
                + ParentArea.upper()
                + ": ["
                + WGname
                + "("
                + acronym.upper()
                + ")]("
                + FilePath
                + ") was  [chartered](https://datatracker.ietf.org/doc/"
                + CharterName
                + ") "
                + LastChange.strftime("%d %B, %Y")
            )
        else:
            print(
                " * "
                + ParentArea.upper()
                + ": "
                + WGname
                + "("
                + acronym.upper()
                + ") was [chartered](https://datatracker.ietf.org/doc/"
                + CharterName
                + ") "
                + LastChange.strftime("%d %B, %Y")
            )
