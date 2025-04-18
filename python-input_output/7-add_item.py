#!/usr/bin/python3
"""add new item"""

import sys
from os.path import exists

saving = __import__('5-save_to_json_file').save_to_json_file
loading = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    items = loading(filename)
except FileNotFoundError:
    items = []
items.extend(sys.argv[1:])

saving(items, filename)
