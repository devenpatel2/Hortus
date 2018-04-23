# Description

This page has notes on different modules for the raspberry-pi

## Config Parser
The config parser contains APIs for parsign the config file. Currently, the [config](index.md#config) has two parts:

1. *"Section"* : This part of the config is used for getting the right topics,
   and the right tags for influxdb. Based on the key and values of various sections, they mqtt subscriper will be setup

e.g
```json 
 "Section":{
	 "Subsection" : [
			{0 : "plant1"},
			{1 : "plant2"}
			]
		},
```

would mean that there would be two x (number of sensors) subscribers . i.e if
there are 3 sensors each per arduino, there would be 2x3 subscribers for recieving data from each of this sensor. 
Assuming these three sensors are - *temperature*, *moisture*, *humidity*, the corresponding MQTT topics for the subscribers would be

```sh
/Section/Subsection/plant1/0/temperature
/Section/Subsection/plant1/0/moisture
/Section/Subsection/plant1/0/humidity
/Section/Subsection/plant1/1/temperature
/Section/Subsection/plant1/1/moisture
/Section/Subsection/plant1/1/humidity
```
 
