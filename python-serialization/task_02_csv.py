#!/usr/bin/python3
import csv, json


def convert_csv_to_json(file_name):

    data = {}
    try:
        with open(file_name, encoding='utf-8') as file:
            reader = csv.DictReader(file)

            data = [row for row in reader]

        with open("data.json", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
        return True
    except FileNotFoundError:
        return False
    except Exception:
        return False
