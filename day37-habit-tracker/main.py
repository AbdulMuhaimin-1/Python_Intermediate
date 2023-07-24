import requests
from datetime import datetime

USERNAME = "muhaimin"
TOKEN = "abdulmu8a1m1nyu551f"
GRAPHID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token" : "abdulmu8a1m1nyu551f",
    "username" : "muhaimin",
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id" : GRAPHID,
    "name" : "Studying",
    "unit" : "min",
    "type" : "int",
    "color" : "ajisai"
}

headers = {
    "X-USER-TOKEN" : TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}"

today = datetime(year=2023, month=7, day=1)
date = today.strftime("%Y%m%d")
# print(today.strftime("%Y%m%d"))

pixel_data = {
    "date" : date,
    "quantity" : "250",
}

# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=pixel_header)
# print(response.text)

pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{date}"

pixel_update = {
    "quantity" : "1200"
}

response = requests.delete(url=pixel_update_endpoint,headers=headers)
print(response.text)
