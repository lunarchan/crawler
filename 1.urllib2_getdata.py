# encoding:utf-8
import urllib.request


def download1(url):
    return urllib.request.urlopen(url).read()


def download2(url):
    return urllib.request.urlopen(url).readlines()

def download3(url):
    response=urllib.request.urlopen(url)
    while True:
        line=response.readline()
        if not line:
            break
        print(line)

url = 'https://search.51job.com/list/000000,000000,0000,00,9,99,java,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
print('1:'+download3(url))
