from bs4 import BeautifulSoup
import requests

#Using BeautifulSoup with live website

response = requests.get("https://news.ycombinator.com/newest")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all(name="a", class_="storylink")

article_text = []
article_link = []

for article in articles:
    link = articles.get("href")
    article_link.append(link)
    text = articles.getText()
    article_text.append(text)
article_votes = [vote.getText().split()[0] for vote in soup.find_all(name='span', class_="score")]
























# with open('website.html', 'r') as file:
#     contents = file.read()


# soup = BeautifulSoup(contents, 'html.parser')
# # print(soup.title.string)

# #Finding all tags 
# all_anchor_tags = soup.find_all(name="a")
# # print(all_anchor_tags)

# # for tags in all_anchor_tags:
# #     #getting all the text
# #     # print(tags.getText())
# #     #getting the link
# #     print(tags.get("href"))

# #finding tags with  class 
# heading = soup.find(name="h3", class_="heading")
# print(heading)