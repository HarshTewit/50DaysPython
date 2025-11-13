import os 
from bs4 import BeautifulSoup
import requests 
import csv

URL = "https://news.ycombinator.com/"
NEWS_FILE = "hacker_news.csv"


def get_news_headers(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status() 
    except:
        print("Failed to generate the response.")
        return[]
    
    soup = BeautifulSoup(response.text, "html.parser")
    post_links = soup.select("span.titleline > a")
    headers = []
    urls = []
    for tag in post_links[:20]:
        text = tag.get_text(strip="True")
        url = tag.get("href").strip()
        headers.append(text)
        urls.append(url)
    
    with open(NEWS_FILE, 'w', encoding="utf-8") as f:
        writer = csv.writer(f)
        for i in range(0, 20):
            writer.writerow([headers[i], urls[i]])
    

    print(headers)



    #print(soup)

get_news_headers(URL)
