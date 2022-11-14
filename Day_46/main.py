from bs4 import BeautifulSoup
import requests
import lxml
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Enter the date
date = input("Enter the date YYYY-MM-DD: ")

CLIENT_ID = "930e2a3db65142d19c1e17a2f0cce094"
CLIENT_SECRET = "ed36f1e8fb43416f97ee58a01f9ba968"

# Requesting the page
response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")
page_html = response.text
soup = BeautifulSoup(page_html, 'lxml')
songs_list = soup.select("li #title-of-a-story")
musics = [songs.text.strip() for songs in songs_list]
print(musics)

