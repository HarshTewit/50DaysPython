import json 
import csv 
import os 

INPUT_FILE = "movies.json"
OUTPUT_FILE = "converted_data.csv"

def load_json_data(filename):
    if not os.path.exists(filename):
        print("The path is not found!")
        return []
    
    with open(filename, 'r', encoding='utf-8') as f:
        try:
            return json.load(f) 
        except:
            print("Invalid JSON Format.")

def convert_to_csv(data, output_file):
    if not data:
        print(type(data))
        print("No data to convert.")
        return 
    
    fieldname = list(data[0].keys()) #data[0] is the first entry in json that can be treated like a dictionary 
    with open (output_file, 'w', encoding='utf-8') as f: 
        try:
            writer = csv.DictWriter(f, fieldnames=fieldname)
            #NOTICE HOW WE CAN USE THE FEILDNAMES IN THE FEILDNAME HEADER 
            writer.writeheader()
            for record in data:
                writer.writerow(record)
        except:
            pass 
    
def main():
    print("Converting JSON to CSV...")
    data = load_json_data(INPUT_FILE)
    convert_to_csv(data, OUTPUT_FILE)

if __name__ == "__main__":
    main()
