# Task 1: Review robots.txt to ensure policy compliance
# I reviewed https://durhamcountylibrary.org/robots.txt
# The assignment scraping steps are not blocked.


# Task 2: Understanding HTML and the DOM

#row cp-search-result-item
#cp-title
#author-link
#manifestation-item-format-cal-wrap available
#manifestation-item-format-info-wrap



# Task 3: Write a program to extract book data

from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import json

options = webdriver.ChromeOptions()
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")

driver = webdriver.Chrome(options=options)

url = "https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart"

driver.get(url)

books = driver.find_elements(
    By.CSS_SELECTOR,
    'li.cp-search-result-item'
)

print(len(books))
results = []

for book in books:

    title_element = book.find_element(
        By.CSS_SELECTOR,
        '.cp-title'
    )

    title = title_element.text


    author_elements = book.find_elements(
        By.CSS_SELECTOR,
        '.author-link'
    )

    authors = []

    for author in author_elements:
        authors.append(author.text)

    author_text = "; ".join(authors)


    format_div = book.find_element(
        By.CSS_SELECTOR,
        '.manifestation-item-format-info-wrap'
    )

    format_year = format_div.text


    book_data = {
        "Title": title,
        "Author": author_text,
        "Format-Year": format_year
    }

    results.append(book_data)
    df = pd.DataFrame(results)
print(df)

df.to_csv("get_books.csv", index=False)

with open("get_books.json", "w") as json_file:
    json.dump(results, json_file, indent=4)