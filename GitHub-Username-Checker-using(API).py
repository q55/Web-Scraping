#its slow , with req.sission it might be faster ...
#closed at 6/12/2022

import requests
import random
import string
import threading
import time
#zl9


def fun():
    while True:
        try:
            first = random.choice(string.ascii_letters)
            second = random.choice(string.digits)
            third = random.choice(string.digits)

            user = first + second + third

            burp0_url = "https://github.com:443/signup_check/username?suggest_usernames=true"
            burp0_cookies = {"_octo": "GH1.1.724805402.1654977106", "logged_in": "no", "tz": "America%2FNew_York",
                             "_gh_sess": "WFYK0F1L%2FCULKoAg5hjKvoY1OzSckEBTFUjXQXabQ%2BObHo6BNVbR1kFU1UANta7Nh9njgLiDq%2BbKQEua3M3bChGiXNldThIFtNwFcnDHsOa1%2FxmciAKY3k9r16LmrZoAjmmPdMFjshMVzPIjH0pTGMSEs9sFca4p9S3%2BvErRyMZozFptlBgZ5hnXtnYHXi7i2qJJOPetkHKGZbgVx0q7Wg2UllUBqGcaexnH9L%2BUWVJJp%2BaVzyUtYvXbTWerLWllUVTG2hbTxAs%2BBXvuMZE9HGLyCouC3ZmfmRoxcN9S7LYWUrQF--CuSxbjxBLma565eU--shl1Ev0JICu6vn0fytnVJA%3D%3D"}
            burp0_headers = {"Sec-Ch-Ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"96\"", "Sec-Ch-Ua-Mobile": "?0",
                             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
                             "Sec-Ch-Ua-Platform": "\"Linux\"",
                             "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundaryWudv2QCMUGzXxJFW",
                             "Accept": "*/*", "Origin": "https://github.com", "Sec-Fetch-Site": "same-origin",
                             "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://github.com/join",
                             "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9"}
            burp0_data = f'------WebKitFormBoundaryWudv2QCMUGzXxJFW\r\nContent-Disposition: form-data; name=\"authenticity_token\"\r\n\r\nO5pIk+0clQRl9V1cFA8E9JRnWDKD72qdpx8SOPtQf9k1vlgGuNw1zvxCsatTSMWlOhz4Wrj3y6ER4x5996uRBQ==\r\n------WebKitFormBoundaryWudv2QCMUGzXxJFW\r\nContent-Disposition: form-data; name=\"value\"\r\n\r\n{user}\r\n------WebKitFormBoundaryWudv2QCMUGzXxJFW--\r\n'

            RandomProxy = random.choice(open('../proxy.txt').read().splitlines())
            # proxies = f'https : http://{RandomProxy}'
            # print(proxies)

            Proxiesid = {
                'http': 'http://{}'.format(RandomProxy),
                'https': 'http://{}'.format(RandomProxy)}

            req = requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data,
                                proxies=Proxiesid)

            if req.status_code == 200:
                print(user + ' user has been found')
            elif 'You have exceeded a secondary rate' in req.text:

                print(req.text)
                print(user + " whoa")
                print(req.status_code)
                #time.sleep(16)
            else:
                # print(req.text)
                print(user + " not avilabl")
                print(req.status_code)
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


