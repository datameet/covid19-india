"""Module to download the number of COVID19 cases from 
Ministry of Health and Family Welfare.

Thejesh GN has already exposed did this and exposed as an API.
This module, just grabs that data and stores in a db.

Note: The timestamps used here are in IST.
"""
import datetime
import itertools
import requests
import sys
import time

from .db import Source
from .utils import setup_logger

URL = "https://data.thejeshgn.com/covid19/_design/india/_view/incidents"

def fetch_covid19_data(**params):
    params.setdefault('nounce', datetime.datetime.utcnow().strftime("%y%m%d%H%M"))
    params.setdefault('descending', 'true')
    data = requests.get(URL, params=params).json()
    rows = [row['value'] for row in data['rows']]
    for key, chunk in itertools.groupby(rows, key=lambda row: row['report_time']):
        timestamp = parse_timestamp(key)
        yield timestamp, [process_row(row) for row in chunk]

def parse_timestamp(datestr):
    return datetime.datetime.strptime(datestr, "%Y-%m-%dT%H:%M:%S.%f%z")

def process_row(row):
    print(row)
    indians = row.get('confirmed_india')
    foreigners = row.get('confirmed_foreign')
    confirmed = row.get('confirmed')
    cured = row['cured']
    active = confirmed - cured
    deaths = row['death']

    return {
        'state_code': row['state'],
        'confirmed': confirmed,
        'active': active,
        'recovered': cured,
        'deaths': deaths,
        'indians': indians,
        'foreigners': foreigners
    }

def download_latest():
    for timestamp, data in fetch_covid19_data(limit=100):
        # Take the most recent one
        return timestamp, data

def download_all():
    return fetch_covid19_data()

def main():
    setup_logger()
    mohfw = Source("mohfw")

    if "--all" in sys.argv:
        for timestamp, data in download_all():
            mohfw.add_new_entry(timestamp, data)
    else:
        timestamp, data = download_latest()
        mohfw.add_new_entry(timestamp, data)

if __name__ == '__main__':
    main()