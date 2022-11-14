from bs4 import BeautifulSoup
import requests

URL = "https://www.amazon.com/Dell-Laptop17-0-inch-Touchscreen-Display-i9-12900HK/dp/B09PHBDT7K/ref=sr_1_3?keywords=dell+xps+17+laptop&qid=1668438108&sprefix=dellxps%2Caps%2C807&sr=8-3"
response = requests.get(url=URL)
html_page = response.text

