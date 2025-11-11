import os 
import json 
import csv 


INPUT_FILE = "weather_logs.csv"
OUTPUT_FILE = "converted_to_json.json"

def load_data(filename):

    if not os.path.exists(filename):
        print("File not found!")
        return []

    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        data = list(reader)
        print(data)
        return data
        """
        list(reader) from csv.DictReader(f) →
        📦 gives you a list of dictionaries, where each dictionary = one row of your CSV file,
        with keys = column headers and values = cell contents.
        """

def save_as_json(data, filename):
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(data, f, indent=2) #just use json . dump 
    print(f"Converted to JSON! {len(data)} records to {filename}")


data = load_data(INPUT_FILE)

load_data(INPUT_FILE)
save_as_json(data, OUTPUT_FILE)