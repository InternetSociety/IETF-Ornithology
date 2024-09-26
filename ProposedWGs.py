#!/usr/bin/env python

import re
import os
import sys
from pathlib import Path
import argparse
import requests
from requests.exceptions import HTTPError
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo


debug =   0


parser = argparse.ArgumentParser(
    prog="AgendaUpdate",
    description="""
                    Lists the working groups in the IETF that are currently proposed
                    """,
    epilog="""Tool specificly developed for the IETF  Ornmithology.
                                           """,
)



# Determine all active groups in IETF

datatrackerUrl = "https://datatracker.ietf.org/api/v1/group/group/?format=json&state=proposed&type=wg&limit=250"

if debug:
    print(datatrackerUrl, file=sys.stderr)
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
        print(datatrackerUrl, file=sys.stderr)
    try:
        response = requests.get(datatrackerUrl)
        response.raise_for_status()
        # access JSOn content
        jsonResponse = response.json()
        if debug > 1:
            print("Entire JSON response", file=sys.stderr)
            print(jsonResponse, file=sys.stderr)

        LastChange = datetime.strptime(
            jsonResponse["time"], "%Y-%m-%dT%H:%M:%S%z"
        )  # Potential bug: not sure about the first index in the object array
        CharterName = jsonResponse["name"]

        CharterRev = jsonResponse["rev"]

    except HTTPError as http_err:
        print(
            f"HTTP error occured while processing {acronym.upper()} and fetching {datatrackerUrl}: {http_err}"
        )
    except Exception as err:
        print(
            f"Other error occured while processing {acronym.upper()} and fetching {datatrackerUrl}: {err}"
        )
    if debug:
        print(LastChange, file=sys.stderr)

 
  
    datatrackerUrl = (
        "https://datatracker.ietf.org" + group["parent"] + "?format=json"
    )
    if debug:
        print(datatrackerUrl, file=sys.stderr)
    try:
        response = requests.get(datatrackerUrl)
        response.raise_for_status()
        # access JSOn content
        jsonResponse = response.json()
        if debug:
            print("Entire JSON response", file=sys.stderr)
            print(jsonResponse, file=sys.stderr)

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
            + ") is being  [chartered](https://datatracker.ietf.org/doc/"
            + CharterName
            + ") "
         
        )
    else:
        print(
            " * "
            + ParentArea.upper()
            + ": "
            + WGname
            + "("
            + acronym.upper()
            + ")  [chartered](https://datatracker.ietf.org/doc/"
            + CharterName
            + ") " 
            )
         
