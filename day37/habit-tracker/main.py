import requests
import os
from datetime import datetime
from dotenv import load_dotenv

# ------------------------------ CREATE USER IN PIXELA API ------------------------------ #

# user_data = {
#     "token": "TjvsxfbJkd01if2nKJc4WN7q",
#     "username": "felipemunozri",
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
# }
#
# response = requests.post("https://pixe.la/v1/users", json=user_data)
# print(response.text)

# ------------------------------ CREATE GRAPH DEFINITION ------------------------------ #

# load_dotenv()
# pixela_username = os.getenv("PIXELA_USERNAME")
# pixela_token = os.getenv("PIXELA_TOKEN")
#
# headers = {
#     "X-USER-TOKEN": pixela_token
# }
#
# graph_config = {
#     "id": "graph1",
#     "name": "Coding Graph",
#     "unit": "Hours",
#     "type": "float",
#     "color": "ajisai"
# }
#
# response = requests.post(f"https://pixe.la/v1/users/{pixela_username}/graphs", json=graph_config, headers=headers)
# print(response.text)

# ------------------------------ GET CREATED GRAPH ------------------------------ #

# visit this url, using the username and the graph id
graph_url = "https://pixe.la/v1/users/felipemunozri/graphs/graph1.html"

# ------------------------------ POST A PIXEL TO THE GRAPH ------------------------------ #

# load_dotenv()
# pixela_username = os.getenv("PIXELA_USERNAME")
# pixela_token = os.getenv("PIXELA_TOKEN")
# graph_id = "graph1"
# today = datetime.now().strftime("%Y%m%d")  # to format dates to yyyyMMdd
#
# headers = {
#     "X-USER-TOKEN": pixela_token
# }
#
# pixel_data = {
#     "date": today,
#     "quantity": "8",  # must be str
# }
#
# response = requests.post(f"https://pixe.la/v1/users/{pixela_username}/graphs/{graph_id}", json=pixel_data,
#                          headers=headers) # we use the post method
# print(response.text)

# ------------------------------ UPDATE A PIXEL IN THE GRAPH ------------------------------ #

load_dotenv()
pixela_username = os.getenv("PIXELA_USERNAME")
pixela_token = os.getenv("PIXELA_TOKEN")
graph_id = "graph1"
today = datetime.now().strftime("%Y%m%d")  # again we pass the date in the endpoint url

headers = {
    "X-USER-TOKEN": pixela_token
}

# we use the delete method and there is no body data, just the header
response = requests.delete(f"https://pixe.la/v1/users/{pixela_username}/graphs/{graph_id}/{today}", headers=headers)

print(response.text)

# ------------------------------ DELETE A PIXEL IN THE GRAPH ------------------------------ #

