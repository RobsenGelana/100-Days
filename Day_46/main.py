from bs4 import BeautifulSoup
import requests
import lxml
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Enter the date
date = input("Enter the date YYYY-MM-DD: ")

# Requesting the page
response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")
page_html = response.text
soup = BeautifulSoup(page_html, 'lxml')
songs_list = soup.select("li #title-of-a-story")
musics = [songs.text.strip() for songs in songs_list]
print(musics)






































# import spotipy
# from spotipy.oauth2 import SpotifyClientCredentials

# birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
# spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

# results = spotify.artist_albums(birdy_uri, album_type='album')
# albums = results['items']
# while results['next']:
#     results = spotify.next(results)
#     albums.extend(results['items'])

# for album in albums:
#     print(album['name'])