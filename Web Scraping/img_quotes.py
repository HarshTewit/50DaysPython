import os
import textwrap
from bs4 import BeautifulSoup
import requests
from PIL import Image, ImageDraw, ImageFont

BASE_URL = "https://quotes.toscrape.com/"
OUTPUT_DIR = "generated_images"


def get_quotes(url):
    quotes = {}
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"There was an error fetching the data: {e}")
        return quotes

    data = BeautifulSoup(response.text, "html.parser")
    quote_tags = data.select("div.quote")[:5]

    for quote in quote_tags:
        qt_text_tag = quote.select_one("span.text")
        author_text_tag = quote.select_one("small.author")

        quote_text = qt_text_tag.get_text(strip=True)
        author_text = author_text_tag.get_text(strip=True)

        quotes[quote_text] = author_text

    return quotes


def create_image(author_name, quote, index):
    width, height = 800, 400
    background_color = "#fdf6e3"
    text_color = "black"

    image = Image.new("RGB", (width, height), background_color)
    draw = ImageDraw.Draw(image)

    font = ImageFont.load_default()
    author_font = ImageFont.load_default()

    wrapped = textwrap.fill(quote, width=60)
    author_text = f"- {author_name}"

    # Draw quote text
    y_text = 60
    draw.text((40, y_text), wrapped, font=font, fill=text_color)

    # Move down depending on number of lines
    y_text += wrapped.count("\n") * 15 + 40

    # Draw author
    draw.text((40, y_text), author_text, font=author_font, fill=text_color)

    # Create output folder
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    filename = os.path.join(OUTPUT_DIR, f"quote_{index + 1}.png")
    image.save(filename)
    print(f"Saved {filename}")


# MAIN EXECUTION
quotes = get_quotes(BASE_URL)
for i, (qt, author) in enumerate(quotes.items()):
    create_image(author, qt, i)
