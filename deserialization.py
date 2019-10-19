#!/usr/bin/env python3
# GitHub: karabin1

import json
import pprint 

with open("data_file.json", "r") as read_file:
    data = json.load(read_file)

pprint.pprint(data)