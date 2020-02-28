import urllib
from http import cookiejar
from urllib import request

#  创建一个对象存储cookie
cookie = cookiejar.CookieJar()
# 自动提取
header = urllib.request.HTTPCookieProcessor(cookie)
# 处理cookie
opener = urllib.request.build_opener(header)
response = opener.open("http://www.baidu.com")
cookies = ""
for data in cookie:
    cookies = cookies + data.name + "=" + data.value + ";\r\n"
print(cookies)


# 保存cookie
filepath = "cookie.txt"
# 设定保存路径
cookie = cookiejar.LWPCookieJar(filepath)
# 设置cookie头
header = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(header)
response = opener.open("http://www.baidu.com")

cookie.save(ignore_expires=True, ignore_discard=True)   # 忽略

# load cookie
filepath = "cookie.txt"
# 设定保存路径
cookie = cookiejar.LWPCookieJar()
cookie.load(filepath, ignore_discard=True, ignore_expires=True)
# 设置cookie头
header = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(header)
response2 = opener.open("http://www.baidu.com")
print(response.read().decode())