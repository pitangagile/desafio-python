import json
import csv
import sys

json_file = open(sys.argv[1])
list_json_pytan = json.load(json_file)

database = []

with open(sys.argv[2]) as csv_file:
    fieldnames = csv_file.readline().split(",")
    fieldnames = [x.rstrip() for x in fieldnames]
    list_json_lactea = csv.DictReader(csv_file, fieldnames)

    for lactea, pytan in zip(list_json_lactea, list_json_pytan):
        database.append({**lactea, **pytan})

with open("database.csv", "w") as csv_out:
    fieldnames = [x for x in database[0].keys()]
    writer = csv.DictWriter(csv_out, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(database)