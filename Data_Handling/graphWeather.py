import matplotlib.pyplot as plt
import csv
from collections import defaultdict

FILE_NAME = "weather_logs.csv"

def visualise_weather():
    date = []
    temps = []
    conditions = defaultdict(int)

    with open(FILE_NAME, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:                
                date.append(row["Date"])
                temps.append(row["Temperature"])
                conditions[row["Condition"]] += 1 #rather bizzare logic 
            except: 
                continue
   
        
        plt.figure(figsize = (10, 7))
        plt.plot(date, temps, marker='o')
        plt.title("Temperature over Time")
        plt.xlabel("Date")
        plt.ylabel("Temperature")
        plt.grid(True)
        plt.show()
    

visualise_weather()
