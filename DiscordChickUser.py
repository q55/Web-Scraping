import requests
import random
import string
import threading
import time
def fun():
    while True :
        try:
            first = random.choice(string.ascii_letters)
            second = random.choice(string.digits)
            third = random.choice(string.digits)

            username = first + second + third
            burp0_url = "https://discord.com:443/api/v9/users/@me/pomelo"
            burp0_cookies = {"locale": "en-US"}
            burp0_headers = {"Sec-Ch-Ua": "\"Chromium\";v=\"113\", \"Not-A.Brand\";v=\"24\"",
                             "X-Debug-Options": "bugReporterEnabled", "Sec-Ch-Ua-Mobile": "?0",
                             "Authorization": "MTEyNTk4NTY1NDAyNzg1Nzk4MA.GmYGHB.C6mCLCbz3DgVZlVa9Yl1Pezxt6RvunZVWb53w8",
                             "X-Discord-Timezone": "Europe/London", "Content-Type": "application/json",
                             "X-Discord-Locale": "en-US", "Sec-Ch-Ua-Platform": "\"Linux\"", "Accept": "*/*",
                             "Origin": "https://discord.com", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "cors",
                             "Sec-Fetch-Dest": "empty", "Referer": "https://discord.com/channels/@me",
                             "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"}
            burp0_json = {"username": username}

            RandomProxy = random.choice(open('../proxy.txt').read().splitlines())
            Proxiesid = {
                'http': 'http://{}'.format(RandomProxy),
                'https': 'http://{}'.format(RandomProxy)}

            req = (requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, json=burp0_json).text)
            print(req)
        except:
            pass




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
