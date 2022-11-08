import requests

endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "asdfhafw1312jasdfa",
    "username": "robsen",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

response = requests.post(url=endpoint, json=user_params)
#test code
print(response.text)