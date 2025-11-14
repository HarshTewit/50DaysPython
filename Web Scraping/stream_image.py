import os 
import requests 
from bs4 import BeautifulSoup
from urllib.parse import urljoin 
import re 


BASE_URL = "https://books.toscrape.com/"
START_PAGE = "catalogue/page-1.html"
OUTPUT_FOLDER = "images"

def sanitize_file_name(title):
    # Keep only safe filename characters
    clean = re.sub(r'[^\w\-_. ]', '', title)
    return clean.replace(" ", "_")

def download_image(img_url, filename):
    try:
        response = requests.get(img_url, stream=True, timeout=10)
        response.raise_for_status()
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)
    except:
        print("There was an error!")

def scrape_download_img():
    url = BASE_URL
    response = requests.get(url)
    data = BeautifulSoup(response.text, "html.parser")
    books = data.select("article.product_pod")[:10] #using select instead of select_one, then truncating the list 

    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)
    
    for book in books:
        title = book.h3.a["title"]
        relative_img_url = book.find("img")["src"].lstrip("../")
        abs_url_img = urljoin(BASE_URL, relative_img_url)
        print(abs_url_img)

        filename = sanitize_file_name(title) + ".jpg"
        filepath = os.path.join(OUTPUT_FOLDER, filename)
        print(filepath)

        print(f"Downloading {title}")
        download_image(abs_url_img, filepath)

scrape_download_img()





