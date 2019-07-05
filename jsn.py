#!/usr/bin/python

import json
with open("data.json","r")as read_file:
	data=json.load(read_file)

print(data["Records"][0]["s3"]["bucket"]["arn"])
