# encoding:utf-8

import urllib.request
import selenium
import selenium.webdriver

#1.抓取网页信息
def get_yiqing_page():

    url = 'https://xw.qq.com/act/fytrace?pgv_ref=wxkyk&ADTAG=wxkyk'
    driver = selenium.webdriver.Chrome("C:/Users/21994/Downloads/chromedriver.exe")
    driver.get(url)
    pagesource = driver.page_source  # 抓取网页源码
    return pagesource
#2.分析并提取

#3.导出为cvs文件