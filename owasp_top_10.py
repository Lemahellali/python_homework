from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from time import sleep

options = webdriver.ChromeOptions()
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")

driver = webdriver.Chrome(options=options)

url = "https://owasp.org/www-project-top-ten/"

driver.get(url)

sleep(2)

links = driver.find_elements(
    By.XPATH,
    '//a[contains(@href, "2021")]'
)

results = []

for link in links[:10]:

    title = link.text
    href = link.get_attribute("href")

    if title and href:

        results.append({
            "Title": title,
            "Link": href
        })

print(results)

df = pd.DataFrame(results)

df.to_csv("owasp_top_10.csv", index=False)

driver.quit()