# Web Scraping with Beautiful Soup

from bs4 import BeautifulSoup
import requests

url = "http://quotes.toscrape.com"

page = requests.get(url)    # Get request to that url
print(page)
# print(page.text)

soup = BeautifulSoup(page.text, "html.parser")
# print(soup.prettify())

# FindAll function to grab a list
# search for tagnames, attributes(kwargs), css class, text strings

# By tagname
titles = soup.findAll(name="title")
print(titles)   # list
print(titles[0])    # just the tag
print(titles[0].text)   # text inside the tag

# By attributes
keywords = soup.findAll(itemprop="keywords")
for word in keywords:
    print(word)

# By css class
quotes = soup.findAll(class_="quote")

for quote in quotes:
    print(quote)

print(quotes[0].prettify())

# By combinations
quotes = soup.findAll("span", class_="text")

for quote in quotes:
    print(quote.text)

quote_list = [x.text for x in quotes]
print(quote_list)

# By text
einsteins = soup.findAll(text="Albert")
for e in einsteins:
    print(e)

# Find quthors
authors = soup.findAll("small", class_="author")
print(authors[0].text)
author_list = [x.text.strip() for x in authors]

# print all my quotes
for i in range(len(quote_list)):
    print()
    print(quote_list[i])
    print("\t-", author_list[i])