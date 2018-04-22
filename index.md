# Introduction

This is documentation for **Hortus** : *an intelligent horticulturist*

## Sample Configuration 

```json
{
"Section":{
	 "Subsection" : [
			{0 : "plant1"},
			{1 : "plant2"}
			]
		},
"Database" :{
	 "ip"     : "influxdb_ip",
	 "user"   : "username",
	 "passwd" : "passwd"
	}
}
```

## Influx data format

```json
[
 {
	 "measurement": "sensor_name",
	 "tags": {
		 "home": "Section",
		 "direction": "Subsection",
		 "pot": "plant1_0"
	 },
	 "time": 1231234131,
	 "fields": {
		 "value": 123.00
	 }
 }
]

```

## MQTT topics
```sh
/Section/Subsection/plant1/0/temperature
/Section/Subsection/plant1/0/mositure
/Section/Subsection/plant1/0/humidity
```
