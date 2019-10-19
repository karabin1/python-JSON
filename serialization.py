#!/usr/bin/env python3
# GitHub: karabin1

import json 

print("complete the data")
name        = input("name: ")
birthplace  = input("birthplace: ")
age         = input("age: ")
education   = input("education: ")
color       = input("favorite color: ")
dish        = input("favorite dish: ")

# add Python object (dict):
data = {
    "name"      : name,
    "birthplace": birthplace,
    "age"       : age,
    "education" : education,
    "color"     : color,
    "dish"      : dish,
}

with open("data_file.json", "w") as write_file:
    json.dump(data, write_file, indent=4)
