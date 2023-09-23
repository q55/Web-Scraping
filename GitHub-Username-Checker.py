import random
import requests
l = 'r','e','z','0'   # You can add any letter that u want
url = 'https://github.com/'

while True:
    random1 = random.choice(l)
    random2 = random.choice(l)
    random3 = random.choice(l)
    random4 = random.choice(l)

    user = random1 + random2 + random3
    urluser = url + user
    req = requests.get(urluser)

    if req.status_code == 404:
        print(user+'<------  user has found')
    else:
        pass


#this program is not accurate ,althogue  it might give u the avilable user .
#could be better using api.