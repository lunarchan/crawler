# coding: utf-8
import urllib.request
import http.cookiejar

cookie = http.cookiejar.CookieJar()

header = urllib.request.HTTPCookieProcessor(cookie)

opener = urllib.request.build_opener(header)
response = opener.open("http://www.renren.com/")

cookies=""
for item in cookie:
    cookies = cookies + item.name + '=' + item.value + '\r\n'

print(cookies)