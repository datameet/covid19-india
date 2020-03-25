# covid19

Random experiements with data related to covid19 cases in India.

## Data Sources

### Ministry of Health and Family Welfare

The Ministry of Health and Family Welfare has been publishing the number of COZID19 cases on their website https://www.mohfw.gov.in/.

Thejesh GN has archived that data periodically and published an API to extract that info.

http://projects.datameet.org/covid19/mohfw/

### The Hindu - COVID19 Dataset

The Hindu is showing up to date count of number of cases per state on its website.

https://www.thehindu.com/sci-tech/health/covid-19-interactive-map-confirmed-cases-in-india/article31041690.ece

## API

The data from these two sources is published as an API. 

The base URL for all these APIs is:

http://covid19-india.anandology.com

### Get Latest Cases

```
GET /cases

{
	"source": "mohfw",
	"last_updated": "2020-03-25T09:15:00+05:30",
	"india": {
	    "active": 521,
	    "confirmed": 562,
	    "deaths": 9,
	    "foreigners": 43,
	    "indians": 519,
	    "recovered": 41
	},
	"states": {
		"ap": {
			"active": 9,
			"confirmed": 9,
			"deaths": 0,
			"foreigners": 0,
			"indians": 9,
			"recovered": 0				
		},
		...
	}
}
```

The default source for this is mohfw (Ministry of Health and Family Welfare). Their data is updated only once or twice a day. 

If you want more live data try adding `?source=thehindu` to get the
data from the hindu website.

### Get cases for a given date

```
GET /cases?date=2020-03-15
...
```

### Get the count of cases by date for India

```
GET /cases/daily

{
  "cases": [
    {
      "active": 521,
      "confirmed": 562,
      "date": "2020-03-25",
      "deaths": 9,
      "foreigners": 43,
      "indians": 519,
      "recovered": 41,
      "timestamp": "2020-03-25T09:15:00+05:30"
    },
    {
      "active": 479,
      "confirmed": 519,
      "date": "2020-03-24",
      "deaths": 10,
      "foreigners": 43,
      "indians": 476,
      "recovered": 40,
      "timestamp": "2020-03-24T20:15:00+05:30"
    },
    ...
   ]
}
```

### Get the count of cases by date for a state

```
GET /cases/daily/mh

{
  "cases": [
    {
      "active": 101,
      "confirmed": 101,
      "date": "2020-03-25",
      "deaths": 2,
      "foreigners": 3,
      "indians": 98,
      "recovered": 0,
      "timestamp": "2020-03-25T09:15:00+05:30"
    },
    {
      "active": 89,
      "confirmed": 89,
      "date": "2020-03-24",
      "deaths": 2,
      "foreigners": 3,
      "indians": 86,
      "recovered": 0,
      "timestamp": "2020-03-24T20:15:00+05:30"
    },
    ...
   ]
}
```

The last part of the URL is the 2-letter state code. You can replace that with whatever state that you are interested.
