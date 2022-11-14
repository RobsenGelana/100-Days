from bs4 import BeautifulSoup
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
    "Accept-Language":"en-US,en;q=0.9"

}
URL = "https://www.amazon.com/Dell-Laptop17-0-inch-Touchscreen-Display-i9-12900HK/dp/B09PHBDT7K/ref=sr_1_3?keywords=dell+xps+17+laptop&qid=1668438108&sprefix=dellxps%2Caps%2C807&sr=8-3"
response = requests.get(url=URL, headers=headers)
html_page = response.text

