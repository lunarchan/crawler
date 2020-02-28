# coding:utf-8
import urllib.request
import http.cookiejar
import urllib.parse
import ssl
url = r'https://im.qq.com/'
formData = {
    'email': '2199426516@qq.com',
    'password': 'www.19961121',
}
data = urllib.parse.urlencode(formData).encode('utf-8')
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0'
}

cookie = http.cookiejar.CookieJar()
cookie_handler = urllib.request.HTTPCookieProcessor(cookie)
httpHandler = urllib.request.HTTPHandler(debuglevel=1)
httpsHandler = urllib.request.HTTPSHandler(debuglevel=1)#访问网络，输出调试信息

# opener = urllib.request.build_opener()
opener = urllib.request.build_opener(httpHandler,httpsHandler,cookie_handler)

context = ssl._create_unverified_context()

request = urllib.request.Request(url=url,data=data,headers=headers)
response = opener.open(request)

print(response.read().decode())
response2 = opener.open('http://www.bejson.com/convert/unicode_chinese/')
print(response2.read().decode())