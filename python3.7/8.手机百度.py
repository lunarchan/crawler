# encoding:utf-8
import urllib.request

def downloadAndroid(url):
    header = {
        "Android QQ": "User-Agent: Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) "
                       "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Mobile Safari/537.36",
        "Connection": "keep-alive"
    }

    request = urllib.request.Request(url, headers=header)
    # page = urllib.request.urlopen(url)
    print(request.get_full_url())#整个网页链接
    print(request.get_method())#get/post
    print(request.host)#服务器域名
    print(request.type)#http或ftp或https
    response = urllib.request.urlopen(request)
    print(response.code)
    print(response.info)
    print(response.read)

downloadAndroid("https://www.baidu.com")