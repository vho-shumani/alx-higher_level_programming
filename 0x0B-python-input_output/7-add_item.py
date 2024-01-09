#!/usr/bin/python3
"""Module dds all arguments to a Python list, and save to file"""


import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    mylist = load_from_json_file("add_item.json")
except FileNotFoundError:
    mylist = [sys.argv[i] for i in range(1, len(sys.argv))]
for i in range(1, len(sys.argv)):
    mylist.append(sys.argv[i] )
save_to_json_file(mylist, "add_item.json")

