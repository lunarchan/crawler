# coding:utf-8
import urllib.request
from urllib.error import URLError


def download(url):
    response = urllib.request.urlopen(url, timeout=10)
    print(type(response))
    print(response.info())
    print(response.read(100))

try:
    print(download("http://www.baidu.com"))
except URLError as e:#抓住错误对象类型当作变量
    print("web Error", e)
