import fitz

FILEPATH = "/Users/harshit/Desktop/50Python/50proj/Web Scraping/sample.pdf"

def read_pdf(file_path):
    doc = fitz.open(file_path)
    all_text = "" #we use this string becauase the doc might have multiple pages 

    for page_num in range(len(doc)):
        page = doc[page_num]
        all_text += page.get_text()

    doc.close()
    return all_text 

if __name__ == "__main__":
    try:
        content = read_pdf(FILEPATH)
        print("-" * 30)
        print(content)
        print("_" * 30)
    except Exception as e:
        print(f"You run into a problem! {e}") 
    