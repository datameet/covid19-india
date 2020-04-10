# Covid19 dashboard for India

Dashboard to explore the Covid19 cases in India.

## Data Sources

### Ministry of Health and Family Welfare

The Ministry of Health and Family Welfare has been publishing the number of COVID19 cases on their website https://www.mohfw.gov.in/.

Thejesh GN has archived that data periodically and published an API to extract that info.

http://projects.datameet.org/covid19/mohfw/

### The Hindu - COVID19 Dataset

The Hindu is showing up to date count of number of cases per state on its website.

https://www.thehindu.com/sci-tech/health/covid-19-interactive-map-confirmed-cases-in-india/article31041690.ece

## API

The data from these two sources is published as an API. 

The base URL for all these APIs is:

http://covid19-india.datameet.org

### Get Latest Cases


Gets the latest number of cases from the [Ministry of Health and Family Welfare][mohfw]. This data is updated not more than couple of times a day.

[mohfw]: https://www.mohfw.gov.in/

```
$ curl http://covid19-india.datameet.org/cases
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

### Get Live Cases

This endpoint similar to `/cases`, except that this uses [The Hindu][thehindu] as source. The Hindu updates the numbers through out of the day from various sources. However, this is not the official stats published by the government.

```
$ curl http://covid19-india.datameet.org/cases/live
{
	...
}
```

The response format of this API endpoint is identical to that of `/cases`.


[thehindu]: https://www.thehindu.com/sci-tech/health/covid-19-interactive-map-confirmed-cases-in-india/article31041690.ece

### Get cases for a given date

```
$ curl http://covid19-india.datameet.org/cases?date=2020-03-15
...
```

### Get the count of cases by date for India

```
$ curl http://covid19-india.datameet.org/cases/daily
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
$ curl http://covid19-india.datameet.org/cases/mh
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
