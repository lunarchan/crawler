# coding:utf-8

import urllib.request
import ssl
import random

user_agent_list = [
    "Mozilla/5.0(Macintosh;IntelMacOSX10.6;rv:2.0.1)Gecko/20100101Firefox/4.0.1",
    "Mozilla/4.0(compatible;MSIE6.0;WindowsNT5.1)",
    "Opera/9.80(WindowsNT6.1;U;en)Presto/2.8.131Version/11.11",
    "Mozilla/5.0(Macintosh;IntelMacOSX10_7_0)AppleWebKit/535.11(KHTML,likeGecko)Chrome/17.0.963.56Safari/535.11",
    "Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1)",
    "Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Trident/4.0;SE2.XMetaSr1.0;SE2.XMetaSr1.0;.NETCLR2.0.50727;SE2.XMetaSr1.0)"
]
context = ssl._create_unverified_context()#忽略安全

# 传统的方法不能访问https
def downloadurl(url):
    formData = {
        'email': '2199426516@qq.com',
        'password': 'www.19961121',
    }
    data = urllib.parse.urlencode(formData).encode('utf-8')
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0'
    }
    request = urllib.request.Request(url,  headers=header)
    response = urllib.request.urlopen(request, context=context)
    return response.read().decode()

print(downloadurl(r'https://xw.qq.com/act/fytrace?pgv_ref=wxkyk&ADTAG=wxkyk'))

#
# url = "https://www.baidu.com"
# headers = {
#     "User-Agent": random.choice(user_agent_list)
# }
# request = urllib.request.Request(url, headers=headers)
# response = urllib.request.urlopen(request, context=context)
# print(response.read().decode())
