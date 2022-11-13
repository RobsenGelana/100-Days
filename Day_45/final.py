from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://www.empireonline.com/movies/features/best-movies-2/")
movies_html = response.text

soup = BeautifulSoup(movies_html, 'html.parser')
all_movies = soup.find_all(name="h3", class_="jsx-4245974604")

movie_title = [movie.getText() for movie in all_movies]
reversed_list = movie_title[::-1]

