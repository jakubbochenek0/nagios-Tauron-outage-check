#! /usr/bin/python
import requests
import json
location  = "Długa"

def check_outage(address):
	response = requests.get("https://www.tauron-dystrybucja.pl/iapi/outage/GetOutages?gaid=904038&type=street")
	
	data = json.loads(response.text)
	when = "never"
	for keyval in data["FutureOutagePeriods"]:
		if(keyval["Message"].find(location) != -1):
			when = keyval["StartDate"]
	for keyval in data["CurrentOutagePeriods"]:
		if(keyval["Message"].find(location) != -1):
			when = "now"
	return when

def main():
	if(check_outage(location) == "now"):
		print("Trwa awaria "+location)
		return 2
	elif(check_outage(location) == "never"):
		print("Brak awarii dla "+location)
		return 0
	else:
		print("Zaplanowana awaria dnia "+check_outage(location)+" dla "+location)
		return 1
	
if __name__ == '__main__':
	main()
