import requests
from datetime import datetime

# https://pixe.la/
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = "INSERT_USERNAME"
TOKEN = "INSERT_TOKEN"
GRAPH = "INSERT_NAME_OF_GRAPH"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# CREATE
# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)

GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

graph_config = {
    "id" : GRAPH,
    "name": "NAME_OF_GRAPH",
    "unit": "days",
    "type": "int",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN": TOKEN
}
# PUT
# response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=headers)
# print(response.text)

PIXELA_CREATION_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH}"
today = datetime.now()
today = datetime(year=2021, month=2, day=23)

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "1"
}
# response = requests.post(url=PIXELA_CREATION_ENDPOINT, json=pixel_data, headers=headers)
# print(response.text)

# UPDATE
new_pixel_data = {
    "quantity": "0"
}

# UPDATE_ENDPONT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH}/'20200224'"
# response = requests.put(url=PIXELA_ENDPOINT, json=new_pixel_data, headers=headers)
# print(response.text)

# DELETE
delete_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH}/'20210223'"
response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)