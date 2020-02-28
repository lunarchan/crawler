# encoding:utf-8
import  urllib.request

httpproxy = urllib.request.ProxyHandler({"http": "112.194.112.239:8118"})#代理无需账号
nohttpproxy = urllib.request.ProxyHandler({})#空代理
opener = urllib.request.build_opener(httpproxy)#创建一个打开器
request = urllib.request.Request("http://www.baidu.com/")#访问百度
response = opener.open(request)#打开网页，内置代理服务器
print(response.read().decode('utf-8'))
