print("============================================================\n")
print("WELCOME TO THE QUOTE SCRAPER\n")
print("============================================================\n")

import requests
from bs4 import BeautifulSoup
from time import sleep
from random import choice
from csv import DictWriter


BASE_URL = "http://quotes.toscrape.com"


def scrape_quotes():
  all_quotes = []
  url = "/page/1"
  while url:
    response = requests.get(f"{BASE_URL}{url}")
    print(f"Now Scraping {BASE_URL}{url}") 
    soup = BeautifulSoup(response.text, "html.parser")
    quotes = soup.find_all(class_="quote")

    for quote in quotes:
      text = quote.find(class_="text").get_text().strip('“”')
      all_quotes.append({
        "text": text,
        "author": quote.find(class_="author").get_text(),
        "link": quote.find('a')["href"]
      })
    # Go to next page
    nxt_button = soup.find(class_='next')
    url = nxt_button.find('a')['href'] if nxt_button else None
    sleep(1)
  print("============================================================\n")
  print(f"{len(all_quotes)} quotes scraped successfully\n\n")
  return all_quotes



#write quotes to csv file
def write_quotes(quotes):
  import io
  with io.open("quotes.csv", "w", newline='', encoding="utf-8") as file:
    headers = ["text","author","link"]
    csv_writer = DictWriter(file, fieldnames=headers)
    csv_writer.writeheader()
    for quote in quotes:
      csv_writer.writerow(quote)

quotes = scrape_quotes()
write_quotes(quotes)