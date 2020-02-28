import urllib.request

# #判断有没有重定向
# response = urllib.request.urlopen("http://www.baidu.cn")
# print(response.geturl()=="http://www.baidu.cn")

class RedirectHander(urllib.request.HTTPRedirectHandler):
    def http_error_302(self, req, fp, code, msg, headers):#重302定向
        res = urllib.request.HTTPRedirectHandler.http_error_301(self, req, fp, code, msg, headers)#重定向后的网页
        res.status = code#返回的编码
        res.newurl = res.geturl()#当前URL
        print(res.newurl, res.status)
        return res

opener = urllib.request.build_opener(RedirectHander)
opener.open("http://www.baidu.cn")