from difflib import SequenceMatcher

STATES = {
	"ap": "Andhra Pradesh",
	"ar": "Arunachal Pradesh",
	"as": "Assam",
	"br": "Bihar",
	"ct": "Chhattisgarh",
	"ga": "Goa",
	"gj": "Gujarat",
	"hr": "Haryana",
	"hp": "Himachal Pradesh",
	"jh": "Jharkhand",
	"ka": "Karnataka",
	"kl": "Kerala",
	"mp": "Madhya Pradesh",
	"mh": "Maharashtra",
	"mn": "Manipur",
	"ml": "Meghalaya",
	"mz": "Mizoram",
	"nl": "Nagaland",
	"or": "Odisha",
	"pb": "Punjab",
	"rj": "Rajasthan",
	"sk": "Sikkim",
	"tn": "Tamil Nadu",
	"tg": "Telangana",
	"tr": "Tripura",
	"ut": "Uttarakhand",
	"up": "Uttar Pradesh",
	"wb": "West Bengal",
	"an": "Andaman and Nicobar Islands",
	"ch": "Chandigarh",
	"dn": "Dadra and Nagar Haveli",
	"dd": "Daman and Diu",
	"dl": "Delhi",
	"jk": "Jammu and Kashmir",
	"la": "Ladakh",
	"ld": "Lakshadweep",
	"py": "Puducherry"
}

STATE_CODES = {name.lower(): code for code, name in STATES.items()}

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def closest_match(name, names):
	return max(names, key=lambda x: similar(x, name))

def get_state_code(name):
	name = name.replace("&", "and").lower()

	if name not in STATE_CODES:
		name = closest_match(name, STATE_CODES.keys())

	return STATE_CODES[name]

def get_state_name(code):
	return STATES[code]