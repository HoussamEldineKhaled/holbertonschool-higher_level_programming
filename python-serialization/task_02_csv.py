#!/usr/bin/python3
import csv, json


def convert_csv_to_json(file_name):

    data = {}
    try:
        with open(file_name, encoding='utf-8') as file:
            reader = csv.DictReader(file)

            data = [row for row in reader]

        serialized_data = json.dumps(data, indent=4)

        with open("data.json", "w", encoding="utf-8") as file:
            json.write(serialized_data)
        return True
    except FileNotFoundError, Exception:
        return False
