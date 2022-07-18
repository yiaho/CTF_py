#爆破已知md5前5位的情况
import hashlib

for i in range(999999, 100000000):
    b = str(i).encode(encoding='utf-8')
    str_md5 = hashlib.md5(b).hexdigest()
    if str_md5[0:6] == '6d0bc1':
        print(str_md5)
        print('It is '+str(i))
        break
    else:
        print(i)