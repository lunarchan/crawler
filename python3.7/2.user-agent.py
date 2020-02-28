# coding:utf-8
import random
import urllib.request
from urllib.error import URLError

# 设置User-Agent列表
user_agent_list = [
    "Mozilla/5.0(Macintosh;IntelMacOSX10.6;rv:2.0.1)Gecko/20100101Firefox/4.0.1",
    "Mozilla/4.0(compatible;MSIE6.0;WindowsNT5.1)",
    "Opera/9.80(WindowsNT6.1;U;en)Presto/2.8.131Version/11.11",
    "Mozilla/5.0(Macintosh;IntelMacOSX10_7_0)AppleWebKit/535.11(KHTML,likeGecko)Chrome/17.0.963.56Safari/535.11",
    "Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1)",
    "Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Trident/4.0;SE2.XMetaSr1.0;SE2.XMetaSr1.0;.NETCLR2.0.50727;SE2.XMetaSr1.0)"
]


def download(url):
    # 从列表中随机取出一个浏览器标识
    headers = {"User-Agent": random.choice(user_agent_list)}
    req = urllib.request.Request(url, headers=headers)  # 发起请求
    data = urllib.request.urlopen(req).read()  # 打开请求，抓取数据
    return data


def download2(url):
    mobileBrowser = "Mozilla/5.0"
    headers = {"User-Agent": mobileBrowser}
    req = urllib.request.Request(url, headers=headers)  # 发起请求
    data = urllib.request.urlopen(req).read()  # 打开请求，抓取数据
    return data


print(download2("https://www.baidu.com"))
