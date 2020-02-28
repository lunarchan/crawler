# coding:utf-8
import urllib.request
import http.cookiejar

filepath = "cookie.txt"
cookie = http.cookiejar.LWPCookieJar(filepath)
header = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(header)
response = opener.open("http://www.baidu.com")

cookie.save(ignore_expires=True, ignore_discard=True)
