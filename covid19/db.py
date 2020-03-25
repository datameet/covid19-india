import web

db = web.database(dbn="postgres", db="covid19")

def get_thehindu_cases():
	"""Returns the cases from most recent entry.
	"""
	cols = "state_code, confirmed, active, deaths, recovered, indians, foreigners"
	entry_id = db.select("covid19_thehindu_entry", order="id desc", limit=1).first().id
	result = db.where("covid19_thehindu", what=cols, entry_id=entry_id)
	return {row.pop('state_code'): row for row in result}
