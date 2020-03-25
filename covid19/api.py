import web
import json
from . import db

urls = (
	"/", "index",
	"/thehindu/cases", "thehindu_cases"
)
app = web.application(urls, globals())
application = app.wsgifunc()

def jsonify(data):
	web.header("Content-type", "application/json")
	return json.dumps(data)

class index:
	def GET(self):
		return jsonify({"app": "covid19-india"})

class thehindu_cases:
	def GET(self):
		cases = db.get_thehindu_cases()

		# keys of the any one entry
		keys = cases['ka'].keys()
		totals = {k: sum(case[k] for case in cases.values()) for k in keys}
		return jsonify({
			"india": totals,
			"states": cases
		})