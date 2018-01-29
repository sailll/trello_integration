import requests

url = "https://api.trello.com/1/webhook/"


callback = "54sailll@gmail.com"

idModel = "586e8f681d4fe9b06a928307"

key = "f94d7697a0a38d6f612dd57f50580f89"

token = "2dae1a7ed3a752c51f62c23c457a4fa651c5222e4ccfc7797076fe16a4ff430e"

querystring = {"callbackURL":callback,"idModel":idModel,"key":key,"token":token}

response = requests.request("POST", url, params=querystring)

print (response.text)