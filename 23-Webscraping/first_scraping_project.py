# =========================================================
# Requests + Beautiful Soup Example
# =========================================================

# Let's scrape data into a CSV! #https://www.rithmschool.com/blog
# Goal: Grab all links from Rithm School blog
# Data: store URL, anchor tag text, and date

# Dependencies 
import requests
from bs4 import BeautifulSoup
from csv import writer

# Get the html
blog_url = "https://www.rithmschool.com"
response = requests.get(blog_url + "/blog")
print("HTML Response Success")

# Make the soup
soup = BeautifulSoup(response.text, "html.parser")

# Extract data from soup
articles = soup.find_all("article") 

# Creating and writing to csv
with open("blog_data.csv", "w") as csv_file:
  csv_writer = writer(csv_file)
  csv_writer.writerow(["title", "link", "date"])
  #LOOPING THROUGH ARTICLES
  for article in articles:
    a_tag = article.find("a")
    #title
    title = a_tag.get_text()
    #url
    url = a_tag["href"]
    #date
    date = article.find("time")["datetime"]
    csv_writer.writerow([title, blog_url + url, date])
    print("CSV FILE created successfully")
