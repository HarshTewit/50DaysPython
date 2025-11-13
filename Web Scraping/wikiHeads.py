

import requests 
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/Python_(programming_language)"
URL_2 = "https://x.com/DrNimoYadav/status/1988832284909142497"

headers_brwsr = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/122.0.0.0 Safari/537.36"
}

def get_h2_headers(url):
    try:
        response = requests.get(url, headers=headers_brwsr, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Failed to fetch page. \n {e}")
        return []
    
    soup = BeautifulSoup(response.text, "html.parser")
    h2_tags = soup.find_all("h2")
    #print(h2_tags)
    headers = []
    for tag in h2_tags:
        header_text = tag.get_text(strip=True) #this is just a fantastic method that will extract the text out of 
        #the page!
        headers.append(header_text)
    
    for h in headers[:10]: 
        print(h)

    #print(headers)
    
get_h2_headers(URL)