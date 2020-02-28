# encoding:utf-8

import urllib.request
import selenium
import selenium.webdriver

import re

def download1(url):
    return urllib.request.urlopen(url).read()

def getnumberbyname(searchname):
    url = 'https://xw.qq.com/act/fytrace?pgv_ref=wxkyk&ADTAG=wxkyk'
          # + searchname + \
          # ',2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
    driver = selenium.webdriver.Chrome("C:/Users/21994/Downloads/chromedriver.exe")
    driver.get(url)
    pagesource = driver.page_source#抓取网页源码
    return pagesource
    restr = """<div class="rt">([\s\S]*?)</div>"""  # 正则表达式，若带括号，则只返回括号内的东西，若正则抓取失败，则可能是因为存在空白字符
    # print(restr)
    regex = re.compile(restr, re.IGNORECASE)
    mylist = regex.findall(pagesource)

    newstr = mylist[0].strip()#前后空格空白符
    restr = """(\\d+)"""
    regex = re.compile(restr, re.IGNORECASE)
    mylist = regex.findall(newstr)
    driver.close()
    if len(mylist)==0:
        return"失败"
    else:
        return mylist[0]

# print(download1(url))
print(getnumberbyname("python"))

# pythonlist=["python","python 运维","python 测试"]
# for pysrt in pythonlist:
#     print(pysrt+":"+getnumberbyname(pysrt))

