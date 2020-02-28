# coding: utf-8

import urllib.request
httpHandler = urllib.request.HTTPHandler(debuglevel=1)
httpsHandler = urllib.request.HTTPSHandler(debuglevel=1)#访问网络，输出调试信息

opener = urllib.request.build_opener(httpHandler,httpsHandler)
urllib.request.install_opener(opener)#全局生效

response = urllib.request.urlopen("http://www.renren.com")