import csv 
import json 
import os 

INPUT_FILE = "sample.json"
OUTPUT_FILE = "sample.csv"

def load_json_data(file):
    if not os.path.exists(file):
        print("JSON NOT FOUND.")
        return []
    
    with open(file, 'r', encoding="utf-8") as f:
        try:
            return json.load(f)
        except:
            print("INVALID JSON FORMAT.")

def convert_to_csv(data, output_file):
    if not data:
        print("NO DATA TO CONVERT")
        return 
    
    feildname = list(data[0].keys)

    with open(output_file, 'w', encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=feildname) #IN CSV WRITING YOU CAN DIRECTLY GIVE IT THE FEILD NAMES 
        writer.writeheader()
        for record in data:
            writer.writerow(record)
        
    print(f"Converted {len(data)} records to {OUTPUT_FILE}")

def main():
    print("Converting JSON to CSV...")
    data = load_json_data(INPUT_FILE)
    convert_to_csv(data, OUTPUT_FILE)

if __name__ == "__main__":
    main()
 