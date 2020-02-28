# coding:utf-8
import urllib.request
import http.cookiejar

filepath = "cookie.txt"
cookie = http.cookiejar.LWPCookieJar()
cookie.load(filepath, ignore_expires=False, ignore_discard=False)

header = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(header)
response = opener.open("http://www.baidu.com")
print(response.read().decode())