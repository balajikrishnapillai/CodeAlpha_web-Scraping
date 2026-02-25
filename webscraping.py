import requests
from bs4 import BeautifulSoup
import pandas as pd
url = "http://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
titles = []
prices = []
ratings = []
availability = []
books = soup.find_all("article", class_="product_pod")
for book in books:
    title = book.h3.a["title"]
    titles.append(title)
    price = book.find("p", class_="price_color").text
    prices.append(price)
    rating = book.p["class"][1]
    ratings.append(rating)
    stock = book.find("p", class_="instock availability").text.strip()
    availability.append(stock)
df = pd.DataFrame({
    "Title": titles,
    "Price": prices,
    "Rating": ratings,
    "Availability": availability
})
df.to_csv("books_data.csv", index=False)
print("Data Scraped Successfully ✅")
print(df.head())