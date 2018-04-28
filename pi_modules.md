# Description

This page has notes on different modules for the raspberry-pi

## Config Parser
The config parser contains APIs for parsign the config file. Currently, the [config](index.md#config) has two parts:

1. *"Section"* : This part of the config is used for getting the right topics,
   and the correct tags for influxdb. Based on the key and values of various sections, the mqtt subscriper will be setup

e.g
```json 
 "Section":{
	 "Subsection" : [
			{0 : "plant1"},
			{1 : "plant2"}
			]
		},
```

The above *Section* would indicate that there would be two \times (number of sensors) subscribers . i.e if
there are 3 sensors each per arduino, there would be 2 \times 3 subscribers for recieving data from each sensor. 
Assuming these three sensors are - *temperature*, *moisture*, *humidity*, the corresponding MQTT topics for the subscribers would be

```sh
/Section/Subsection/plant1/0/temperature
/Section/Subsection/plant1/0/moisture
/Section/Subsection/plant1/0/humidity
/Section/Subsection/plant1/1/temperature
/Section/Subsection/plant1/1/moisture
/Section/Subsection/plant1/1/humidity
```
Typical use case would be 
```python

for plants in parser

	topic = parser.get_topic(plant):
	
```

2. *"DB"* : This part of the config has the neccesary details for establishing connection with influx database

```json
"Database" :{
	 "ip"     : "influxdb_ip",
	 "user"   : "username",
	 "passwd" : "passwd"
	}
}
```

## Logging

The logging module provides logging api. The logs are printed in systemd journals format.

```python
FORMAT = '%(asctime)-15s [%(name)s] [%(levelname)s] %(message)s'
```
## Influx

## MQTT

## Data Logger

## Data Uploader

# Links
1. [Home](index.md)
2. [To-Dos](todos.md)

