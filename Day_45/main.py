from bs4 import BeautifulSoup

with open('website.html', 'r') as file:
    contents = file.read()


soup = BeautifulSoup(contents, 'html.parser')
# print(soup.title.string)

#Finding all tags 
all_anchor_tags = soup.find_all(name="a")
print(all_anchor_tags)

for tags in all_anchor_tags:
    #getting all the text
    print(tags.getText())