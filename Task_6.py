#Task 6 - Web Scraping 

import requests
from bs4 import BeautifulSoup

def scrape_quotes():
    url = "http://quotes.toscrape.com"
    try:
        response = requests.get(url)
        response.raise_for_status() 
    except requests.RequestException as e:
        print(f"Error fetching website: {e}")
        return

    soup = BeautifulSoup(response.text, "html.parser")
    quotes = soup.find_all("div", class_="quote")

    print("\nTop Quotes from http://quotes.toscrape.com:\n")
    for idx, quote in enumerate(quotes, start=1):
        text = quote.find("span", class_="text").text
        author = quote.find("small", class_="author").text
        tags = [tag.text for tag in quote.find_all("a", class_="tag")]
        print(f"{idx}. \"{text}\"\n   — {author} (Tags: {', '.join(tags)})\n")

if __name__ == "__main__":
    scrape_quotes()
