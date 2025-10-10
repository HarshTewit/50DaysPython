import csv
import os 
from datetime import datetime
import requests 

FILE_NAME = "weather_logs.csv"
city_name = ""
API_key = "f5a5f97a366043f3192f273edc10d43c" #keys are usually hidden 



#URL = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}"

if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(["Date", "City", "Temperature", "Condition"])

def log_weather():
    city = input("Enter your city name. ").strip()
    date = datetime.now().strftime("%Y-%m-%d")

    #prevent duplicate entries for the same city on the same day
    with open(FILE_NAME, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["Date"] == date and row["City"].lower() == city.lower(): 
                print("City and Date details already logged!")
                return
    
    #now we will go and get our data from the API which we will enclose ina try and catch 
    try:
        URL = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}"
        response = requests.get(URL) 
        #the response is a string- but technically a JSON Object. So we will have to convert that. 
        data = response.json()
        #all data comes in with a status code 
        if response.status_code != 200:
            print(f"API ERROR!")
        
        temp = data["main"]["temp"]
        condition = data["weather"][0]["description"]

        #now write this into your csv 
        with open(FILE_NAME, "a") as f:
            writer = csv.writer(f)
            writer.writerow([date, city, temp, condition])
            print("Weather Logged!")
             

    except Exception as e:
        print("Failed to make an API Call.")

def show_report(): 
    with open(FILE_NAME, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

def main():
    while True:
        print("**REAL TIME WEATHER LOGGER**")
        print("1. Add Weather Log. ")
        print("2. See report.")
        print("3. Exit")

        choice = input("Choose a choice 1-3.").strip()
        match choice:
            case "1":
                log_weather()
            case "2":
                show_report()
            case _:
                break

main()



