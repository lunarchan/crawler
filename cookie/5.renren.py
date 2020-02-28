# -*- coding:utf-8 -*-
from urllib import request as urllib2
from urllib import parse
from http import cookiejar

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0'
}
formData = {
    'email': '18985177696',
    'password': 'www.19961121',
}
data = parse.urlencode(formData).encode('utf-8')
url = r'http://www.renren.com/PLogin.do'

cookie = cookiejar.CookieJar()
cookie_handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(cookie_handler)
request = urllib2.Request(url=url,data=data ,headers=headers)
response = opener.open(request)
print(response.read().decode())

response2 = opener.open('http://www.renren.com/963457938/profile')
print(response2.read().decode())
