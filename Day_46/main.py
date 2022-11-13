from bs4 import BeautifulSoup
import requests
import lxml

# Enter the date
date = input("Enter the date YYYY-MM-DD: ")

# Requesting the page
response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")
page_html = response.text
soup = BeautifulSoup(page_html, 'lxml')
songs_list = soup.select("li #title-of-a-story")
musics = [songs.text.strip() for songs in songs_list]
print(musics)
