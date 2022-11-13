import requests
from bs4 import BeautifulSoup
from datetime import datetime


URL = 'https://www.billboard.com/charts/hot-100/'
response = requests.get(url=URL)
music_html = response.text

soup = BeautifulSoup(music_html, 'html.parser')
music_list = soup.find(name="use")

# user_input = input("what year you would like to travel to in YYY-MM-DD: ")