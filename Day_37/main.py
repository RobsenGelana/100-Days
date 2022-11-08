import requests

TOKEN = "asdfhafw1312jasdfa"
USERNAME = "robsen"
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
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "hours",
    "type": "float",
    "color": "momiji",
}
http_header = {
    "X-USER-TOKEN": TOKEN
}

response = requests.post(url=graph_endpoint, json=graph_conf)
print(response.text)