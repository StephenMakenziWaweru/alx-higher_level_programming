#!/usr/bin/python3
"""Module for a script that adds all arguments to a Python list"""
import json
from sys import argv
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


file_name = "add_item.json"

# can also use os.path.exists(file) for try and except
# be sure to import os.path
try:
    json_list = load_from_json_file(file_name)
except:
    json_list = []
for item in argv[1:]:
    json_list.append(item)

save_to_json_file(json_list, file_name)
