import web
import json
from .db import Source

urls = (
	"/", "index",
	"/cases", "cases",
	"/cases/daily", "daily_cases",
	"/cases/daily/(.*)", "daily_cases",

	# legacy
	"/thehindu/cases", "thehindu_cases"
)

app = web.application(urls, globals())
application = app.wsgifunc()

def jsonify(data):
	web.header("Content-type", "application/json")
	return json.dumps(data, indent="  ", sort_keys=True)

class index:
	def GET(self):
		return jsonify({
			"app": "covid19-india",
			"repo_url": "https://github.com/anandology/covid19",
		})

class cases:
	def GET(self):
		i = web.input(date=None)
		source = get_source()
		return jsonify(source.get_cases(date=i.date))

class daily_cases:
	def GET(self, state=None):
		source = get_source()
		return jsonify(source.get_daily_cases(state=state))


class thehindu_cases:
	def GET(self):
		raise web.redirect("/cases?source=thehindu")

def get_source():
	i = web.input(source="mohfw")
	if i.source not in ["mohfw", "thehindu"]:
		i.source = "mohfw"
	return Source(i.source)