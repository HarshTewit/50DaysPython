import json
import os 
import csv 

INPUT_FILE = "/Users/harshit/Desktop/50Python/50proj/Data_Handling/my_sample.json"
OUTPUT_FILE = "flattened_json.json"

def flatten_json(data, parent_key="", seperator="_"):
    #at the end of the day i have to create a dictionary! 
    items = {} #empty dictionary 

    """
    Do i handle a dictionary or an array? 
    isinstance(data, data_type) checks and returns true if data is of the specified data_type 
    """
    if isinstance(data, dict):
        for key, value in data.items():
            full_key = f"{parent_key}{seperator}{key}" if parent_key else key 
            print(full_key)
            items.update(flatten_json(value, full_key, seperator=seperator))
    elif isinstance(data, list):
        for idx, item in enumerate(data):
            full_key = f"{parent_key}{seperator}{idx}" if parent_key else str(idx)
            print(full_key)
            items.update(flatten_json(item, full_key, seperator=seperator))
    else:
        items[parent_key] = data

    return items 


def main():
    if not os.path.exists(INPUT_FILE):
            print("No input file found.")
            return 
        
    try:
        with open(INPUT_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        sep = input("Enter your seperator, like _ or - or .").strip() or '.'
        
        flattened= flatten_json(data, seperator=sep)

        with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
            json.dump(flattened, f, indent=2)

        print("The flattenning of json is successful.")


    except Exception as e:
        print(f"Failed to flatten the data beacuse of {e} ")
        
if __name__ == "__main__":
    main()