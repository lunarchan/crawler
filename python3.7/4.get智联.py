# coding:utf-8
import urllib.request
from urllib.error import URLError
import urllib.parse


def download(addr, mytype):
    url = "https://zhaopin.baidu.com/quanzhi?"
    word = {"city": addr, "query": mytype}
    word = urllib.parse.urlencode(word)
    url = url + word
    response = urllib.request.urlopen(url, timeout=10)
    data = response.read().decode()
    print(response.code)
    return data

try:
    addr = "深圳"
    mytype = 'python'
    # download(addr, mytype)
    print(download(addr, mytype))
except URLError as e:#抓住错误对象类型当作变量
    print("web Error", e)
