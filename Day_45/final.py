from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
# print(response)
movie_data = response.text

#test code
print(movie_data)
soup = BeautifulSoup(movie_data, "html.parser")
data_outputs = soup.find_all(name="h3", class_="jsx-4245974604")

movie_list = []

for i in data_outputs:
    text = i.getText()
    # print(type(text))
    movie_list.append(text)

# print(movie_list)