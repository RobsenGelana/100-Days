import requests
from datetime import datetime


TOKEN = "asdfhafw1312jasdfa"
USERNAME = "robsen"
ID = "graph1"
endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=endpoint, json=user_params)
#test code
# print(response.text)

graph_endpoint = f"{endpoint}/{USERNAME}/graphs"

graph_conf = {
    "id": ID,
    "name": "Coding Graph",
    "unit": "hours",
    "type": "float",
    "color": "momiji",
}
http_header = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_conf, headers=http_header)
# print(response.text)
today = datetime.now()
graph_value = f"{graph_endpoint}/{ID}"

graph_value_config = {
    'date': today.strftime("%Y%m%d"),
    'quantity': "11.7",
}

# response = requests.post(url=graph_value, json=graph_value_config, headers=http_header)
# print(response.text)

#Updating the pixel

update_endpoint = f"{graph_value}/20220924"
update_json = {
    "quantity": "9.89"
}
# response = requests.put(url=update_endpoint, json=update_json, headers=http_header)
# print(response.text)

#Deleting pixel

delete_endpoint = f"{graph_value}/20220724"

response = requests.delete(url=delete_endpoint, headers=http_header)
print(response.text)