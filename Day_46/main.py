import requests
from bs4 import BeautifulSoup
from datetime import datetime


user_input = input("what year you would like to travel to in YYY-MM-DD: ")
URL = 'https://www.billboard.com/charts/hot-100/' + user_input
response = requests.get(url=URL)
music_html = response.text

soup = BeautifulSoup(music_html, 'html.parser')
music_list = soup.find_all(name="h3", class_="c-title")
songs = [music.getText().strip() for music in music_list]
print(songs)
