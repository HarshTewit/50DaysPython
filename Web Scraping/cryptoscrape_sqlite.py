import os 
import csv 
from datetime import datetime
import requests 
import json
import matplotlib.pyplot as plt 
import time 
import sqlite3 

import schedule 

API_URL = "https://api.coingecko.com/api/v3/coins/markets"

PARAMS = {
    'vs_currency': "usd",
    "order": 'market_cap_desc',
    "per_page":10,
    'page':1,
    'sparkline':False
    }

DB_NAME = "crypto.db"

def fetch_crypto_data():
    response = requests.get(API_URL, params=PARAMS)
    data = response.json()
    #print(data)
    with open("CRYPTODATA.json", 'w') as f:
        json.dump( response.json(), f, indent = 4)
    return data

def create_table():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor() 
    #cursor.execute("DROP TABLE IF EXISTS crypto_prices")
    #now we may execute any SQL using this cursor 
    cursor.execute(''' 
                   CREATE TABLE IF NOT EXISTS crypto_prices (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   timestamp TEXT,
                   coin TEXT,
                   price REAL 
                   )
                   ''')
    conn.commit()
    conn.close()

def save_to_database(data):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    timestamp = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    for coin in data:
        cursor.execute('''
                       INSERT INTO crypto_prices(timestamp, coin, price)
                       VALUES(?, ?, ?)
                       ''', (timestamp, coin['id'], coin['current_price']))
    
    conn.commit()
    conn.close()
    print("Price saved to database")

def search_coin(coin_name):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute( #cursor is perfectly capable of storing the result itself. Do not need to create a variable
        '''
SELECT * FROM crypto_prices 
WHERE coin = ?
ORDER BY timestamp DESC 
LIMIT 1
''', (coin_name, ))
    result = cursor.fetchone()
    #print(f"RESULT RAW IS {result}")
    if result:
        print(f"Latest price for {coin_name}: ${result[3]}")
    else:
        print("Coin not found!")

    conn.close()



# def job():
#     print("Fetching hourly data!..")
#     crypto_data = fetch_crypto_data()
#     save_to_csv(crypto_data)

# schedule.every().hour.do(job)

# while True:
#     schedule.run_pending()
#     time.sleep(1)

def main():
     create_table()
     print("1. Fetch and Store Crypto Data")
     print("2. Search latest Crypto Data")

     choice = input("Choose an option").strip()
     if choice == "1":
         data = fetch_crypto_data()
         save_to_database(data)
     else:
         coin_name = input("Enter coint name ").strip().lower()
         search_coin(coin_name)


if __name__ == "__main__":
    main()
#fetch_crypto_data()