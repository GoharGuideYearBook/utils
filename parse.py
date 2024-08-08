import csv
import json

def get_dict(csv_file_path):
    data = []
    with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data.append({
                "name": row["What's your Discord username?"],
                "role": "Alumni Staff",
                "quote": row["Leave a quote for the yearbook. Make sure your quote doesn't exceed over 100 characters!"],
                "img": "images/" + row["What's your Discord username?"] + ".webp"
            })
    return data

def get_json(data, json_file_path):
    with open(json_file_path, mode='w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)

a = get_dict("test.csv")
get_json(a, "people.json")