import os 
import csv 
from datetime import datetime
import requests 
import json
import matplotlib.pyplot as plt 

API_URL = "https://api.coingecko.com/api/v3/coins/markets"

PARAMS = {
    'vs_currency': "usd",
    "order": 'market_cap_desc',
    "per_page":10,
    'page':1,
    'sparkline':False
    }

CSV_FILE = "crypto_prices.csv"

def fetch_crypto_data():
    response = requests.get(API_URL, params=PARAMS)
    data = response.json()
    #print(data)
    with open("CRYPTODATA.json", 'w') as f:
        json.dump( response.json(), f, indent = 4)
    return data


def save_to_csv(data):
    file_exists = os.path.isfile(CSV_FILE)
    coin = fetch_crypto_data()

    with open(CSV_FILE, 'a', encoding="utf-8") as f:
        writer = csv.writer(f)
        if not file_exists:
            #i will write the headers of the file 
            writer.writerow(["timestamp", "coin", "price"])
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        for coin in data:
            writer.writerow([timestamp, coin["id"], coin["current_price"]])
    
    print("DATA SAVED!")

def plot_graph(coin_id):
    times = []
    prices = []

    with open(CSV_FILE, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["coin"] == coin_id:
                times.append(row['timestamp'])
                prices.append(row['price'])
        
        if not times:
            print(f"No data found for {coin_id}")
            return 
        
        plt.figure(figsize=(10,5))
        plt.plot(times, prices, marker='o')
        plt.tight_layout()
        plt.grid()
        plt.show()

def main():
    print("Fetching Crypto Data Live!")
    crypto_data = fetch_crypto_data()
    save_to_csv(crypto_data)


    print("-" * 30)
    for coin in crypto_data:
        print(f"{coin['id']} - ${coin['current_price']}")
    print("-" * 30)

    user_coin = input("Enter the coin name to get the graph").strip().lower()

    if user_coin:
        plot_graph(user_coin)

if __name__ == "__main__":
    main()
#fetch_crypto_data()