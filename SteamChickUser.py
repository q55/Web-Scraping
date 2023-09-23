import requests
import random
import string
import threading
session = requests.session()

burp0_url = "https://store.steampowered.com:443/join/checkavail/"
burp0_cookies = {"browserid": "4719228550303115735", "timezoneOffset": "-14400,0", "_ga": "GA1.2.162472225.1659790660", "_gid": "GA1.2.247765550.1659911056", "steamCountry": "SA%7C64eeb025573a4bc91b72db982860ecc4", "sessionid": "f7d1c80159454820456316f0", "app_impressions": "251570@1_4_4__139_4|221100@1_4_4__139_4|1506830@1_4_4__139_4|1151640@1_4_4__139_4|247080@1_4_4__40_3|2110180@1_4_4__40_3|903950@1_4_4__40_2|2110220@1_4_4__40_2|2102910@1_4_4__40_1|862860@1_4_4__40_1"}
burp0_headers = {"Sec-Ch-Ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"96\"", "Sec-Ch-Ua-Mobile": "?0", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "Accept": "text/javascript, text/html, application/xml, text/xml, */*", "X-Prototype-Version": "1.7", "X-Requested-With": "XMLHttpRequest", "Sec-Ch-Ua-Platform": "\"Linux\"", "Origin": "https://store.steampowered.com", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://store.steampowered.com/join/completesignup?creationid=1018046924380250701", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9", "Connection": "close"}


def fun():

    while True:
        try:
            first = random.choice(string.ascii_letters)
            second = random.choice(string.digits)
            third = random.choice(string.digits)
            fourth = random.choice(string.digits)
            username = first + second + third + fourth
            i = 'o488'
            burp0_data = {"accountname": f'{username}', "count": "3"}

            RandomProxy = random.choice(open('../proxy.txt').read().splitlines())
            Proxiesid = {
                'http': 'http://{}'.format(RandomProxy),
                'https': 'http://{}'.format(RandomProxy)}

            req = session.post(burp0_url, data=burp0_data,
                               proxies=Proxiesid)
            print(req.text)

            if '{"bAvailable":true,"rgSuggestions":[]}' in req.text:
                print(username + '<----- Available')
            else:
                pass

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



#not working with some id's-------> fix it in req.text
#u483<----- Available
#O488<----- Available
#O860<----- Available
#o890
