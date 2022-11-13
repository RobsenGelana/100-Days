from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
movie_data = response.text

soup = BeautifulSoup(response, "html.parser")
df = soup.find_all(name="h3", class_="jsx-4245974604")