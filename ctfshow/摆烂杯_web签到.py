import requests

url = 'http://71aca5d1-f2be-48be-9fc9-4574cf6e9b8c.challenge.ctf.show/'

for i in range(1,10):
    for j in range(1,10):
        for k in range(1,10):
            data = {
                'A':i,
                'B':j,
                'C':k,
            }
            res = requests.post(url=url,data=data)
            #print(res.text)
            print(k)
            if '请输入三个整数' not in res.text:
                print(str(i)+str(j)+str(k))
                exit()