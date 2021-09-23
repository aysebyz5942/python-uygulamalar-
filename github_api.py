import requests
import json

token="************************" #not going to tell you mine
response=requests.get("https://api.github.com/user",params={"access_token":token})
data=json.loads(response.content) #json olarak alınabiliyor ve kullanılabiliyor
print(data)
#kullanıcıya ait verileri alıyor
github_user="sauymaz"
endpoint=f"https://api.github.com/users/{github_user}/repos"
repos=json.loads(requests.get(endpoint).text) #tokensız çekilebiliyor
print(repos)