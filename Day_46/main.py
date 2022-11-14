from bs4 import BeautifulSoup
import requests
import lxml
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth

# Enter the date
date = input("Enter the date YYYY-MM-DD: ")

# Requesting the page
response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")
page_html = response.text
soup = BeautifulSoup(page_html, 'lxml')
songs_list = soup.select("li #title-of-a-story")
musics = [songs.text.strip() for songs in songs_list]
print(musics)


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://localhost8888/callback/",
        client_id="930e2a3db65142d19c1e17a2f0cce094",
        client_secret="ed36f1e8fb43416f97ee58a01f9ba968",
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
song_names = []
song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")


































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