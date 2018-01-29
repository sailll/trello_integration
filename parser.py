import requests
import json


url = "https://api.trello.com/1/actions/"

action_id = "55411859be21b8ad7dcd4c78"

url = url + action_id

key = "f94d7697a0a38d6f612dd57f50580f89"

token = "2dae1a7ed3a752c51f62c23c457a4fa651c5222e4ccfc7797076fe16a4ff430e"

querystring = {"key":key,"token":token}

response = requests.request("GET", url, params=querystring)
action = json.loads(response.text)
print(action)