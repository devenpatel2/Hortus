# Introduction

This is documentation for **Hortus** : *an intelligent horticulturist*
Below is an overview of the architecture of the system. 

![alt text](/images/architecture-v1.png "Overview")

## Configs 
This section has all the basic configs and communication topics


### Sample Configuration 

Here is a sample config for the setup of app running on local unit that communicates with remote db.

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

### Influx data format

Sample Influx db message body

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

### MQTT topics
```sh
/Section/Subsection/plant1/0/sensor_name
```

## Links
[TO-DOs](todos.md)
