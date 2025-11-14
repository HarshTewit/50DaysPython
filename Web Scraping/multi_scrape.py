import requests
import os 
from bs4 import BeautifulSoup
import json 
from urllib.parse import urljoin

BASE_URL = "https://books.toscrape.com/"
START_PAGE = "catalogue/page-1.html"
OUTPUT_FILE = "books_data.json"
BOOK_COUNT = 70

def scrape_page(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Cannot fetch data, {e}")
        return [], None #the strategy is to return the array, and the url of the next page 
    
    data = BeautifulSoup(response.text, "html.parser")
    books = []
    title = []
    prices = []

    url_holder = data.select_one("li.next > a")
    next_url = urljoin(url, url_holder.get("href")) if url_holder else None

    for article in data.select("article.product_pod"):
        title_tag = article.select_one("h3 > a")
        title = title_tag.get("title")
        price = article.select_one("p.price_color").text.strip() 
        books.append(f"{title} - {price} : {next_url}")
    
    return books, next_url
        

def main():
    collected = []
    current_url = urljoin(BASE_URL, START_PAGE)

    while(len(collected) < BOOK_COUNT and current_url):
        print(f"Scrapping {current_url} \n")
        books, next_url = scrape_page(current_url)
        collected.extend(books)
        current_url = next_url
    
    with open(OUTPUT_FILE, 'w', encoding="utf-8") as f:
        json.dump(collected, f, indent=2)
    
 


main()