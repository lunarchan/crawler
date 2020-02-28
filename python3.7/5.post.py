# encoding:utf-8
import random
import urllib.request
import urllib.parse

user_agent_list = [
    "Mozilla/5.0(Macintosh;IntelMacOSX10.6;rv:2.0.1)Gecko/20100101Firefox/4.0.1",
    "Mozilla/4.0(compatible;MSIE6.0;WindowsNT5.1)",
    "Opera/9.80(WindowsNT6.1;U;en)Presto/2.8.131Version/11.11",
    "Mozilla/5.0(Macintosh;IntelMacOSX10_7_0)AppleWebKit/535.11(KHTML,likeGecko)Chrome/17.0.963.56Safari/535.11",
    "Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1)",
    "Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Trident/4.0;SE2.XMetaSr1.0;SE2.XMetaSr1.0;.NETCLR2.0.50727;SE2.XMetaSr1.0)"
]

data = {"first": "true", "p": "1", "kd": "python"}
params = "?"
for key in data:
    params = params + key + "=" + data[key] + "&"
data = urllib.parse.urlencode(data).encode('utf-8')
header = {"User-Agent": random.choice(user_agent_list)}
url = "https://www.lagou.com/"

req = urllib.request.Request(url, headers=header, data=data)#post方法
#req =  urllib.request.Request(url+params)#post方法
page = urllib.request.urlopen(req).read()
page = page.decode('utf-8')

print(page)
