import requests
import random
import string
import threading
burp0_url = "https://gql.twitch.tv:443/gql"
burp0_headers = {"Sec-Ch-Ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"96\"", "Accept-Language": "en-US", "Sec-Ch-Ua-Mobile": "?0", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36", "Content-Type": "text/plain;charset=UTF-8", "Client-Id": "kimne78kx3ncx6brgo4mv6wki5h1ko", "X-Device-Id": "MhQoojGssCy24C2m2gos02aVBwAyFX4g", "Sec-Ch-Ua-Platform": "\"Linux\"", "Accept": "*/*", "Origin": "https://www.twitch.tv", "Sec-Fetch-Site": "same-site", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://www.twitch.tv/", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
def fun():

    while True:
        first = random.choice(string.ascii_letters)
        second = random.choice(string.digits)
        third = random.choice(string.digits)

        username= first + second + third + third
        burp0_json = [{"extensions": {
            "persistedQuery": {"sha256Hash": "fd1085cf8350e309b725cf8ca91cd90cac03909a3edeeedbd0872ac912f3d660",
                               "version": 1}}, "operationName": "UsernameValidator_User",
                       "variables": {"username": username}}]
        req = requests.post(burp0_url, headers=burp0_headers, json=burp0_json)

        if 'isUsernameAvailable":true' in req.text :
            print(username + '<----- Available')
        else:
            pass
            #print(username + ' <-------- Bad')



number = int(input('Theard: '))
Threads = []
def repates():
    global number
for i in range(number):
    t = threading.Thread(target=fun)
    t.start()
    Threads.append(t)

for mi in Threads:
    mi.join()

while True:
    repates()



#t222<----- Available
#[{"errors":[{"message":"service error","path":["isUsernameAvailable"]}],"data":{"isUsernameAvailable":null},"extensions":{"durationMilliseconds":4,"operationName":"UsernameValidator_User","requestID":"01G8NQ9QKDSWH6S4YJY8J1P85W"}}]
