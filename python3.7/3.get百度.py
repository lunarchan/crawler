# coding: utf-8

import urllib.parse
import urllib.request

# word = {"wd": "尹成"}
# print("url解码："+urllib.parse.unquote('%E5%B0%B9%E6%88%90'))
# print("url编码："+urllib.parse.urlencode(word))

url = "http://www.baidu.com/s"
word = {"wd": "尹成"}
word = urllib.parse.urlencode(word)#编码成字符串
newUrl = url + "?" + word
request = urllib.request.Request(newUrl)#发起请求
print(urllib.request.urlopen(request))#打开页面读取信息
