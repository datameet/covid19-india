"""Program to download and extract the data containing covid-19 cases
in India by state from The Hindu website.
"""
import requests
import re
import json
import sys
from pathlib import Path
import datetime
import logging
import web
from . import states

URL = "https://public.flourish.studio/visualisation/1538247/embed?auto=1"

ROOT = Path(__file__).parent.parent / "data"

logger = logging.getLogger(__name__)

db = web.database(dbn="postgres", db="covid19")
TABLE = "covid19_thehindu"
ENTRY_TABLE = "covid19_thehindu_entry"

def download() -> Path:
	"""Downloads the raw data and returns the path to the downloaded file.
	"""
	ROOT.mkdir(exist_ok=True)

	now = datetime.datetime.utcnow()
	filename = now.strftime("%y%m%d-%H%M%S.html")
	path = ROOT / filename

	logger.info("downloading the raw data...")	
	html = requests.get(URL).text
	
	# Archive raw data
	logger.info("writing the raw data to %s", path)	
	path.write_text(html, encoding="utf-8")
	return now, html

def parse_columns(html):
	re_columns = re.compile(r"_Flourish_data_column_names\s+= (.*}),")
	match = re_columns.search(html)
	jsondata = match.group(1)
	columns = json.loads(jsondata)['choropleth']['metadata']
	return [c.lower().strip().replace(" ", "_") for c in columns]

def parse_data(html):
	re_data = re.compile(r"_Flourish_data = (.*});", re.DOTALL);
	match = re_data.search(html)
	jsondata = match.group(1)
	d = json.loads(jsondata)
	return d['choropleth']

def parse(html):
	columns = parse_columns(html)
	all_states = parse_data(html)
	result = []
	for state in all_states:
		metadata = [x and int(x) or 0 for x in state['metadata']]
		d = dict(zip(columns, metadata))
		d['name'] = state['name']
		d['state_code'] = states.get_state_code(state['name'])
		result.append(d)
	return result

def setup_logger():
    logging.basicConfig(
        level=logging.INFO,
        format='[%(asctime)s] %(message)s',
        datefmt='%H:%M:%S')

def load_db(timestamp, data):
	logger.info("loading data into the db...")
	with db.transaction():
		entry_id = db.insert(ENTRY_TABLE, timestamp=timestamp)
		data = [_process_row(row, entry_id) for row in data]
		db.multiple_insert(TABLE, data)

def _process_row(row, entry_id):
	return {
		'entry_id': entry_id,
		'state_code': row['state_code'],
		'confirmed': row['confirmed_cases'],
		'active': row['active_cases'],
		'recovered': row['recovered'],
		'deaths': row['deaths'],
		'indians': row['indians'],
		'foreigners': row['foreigners']
	}

def main():
	setup_logger()
	timestamp, html = download()
	data = parse(html)
	load_db(timestamp, data)

if __name__ == '__main__':
	main()