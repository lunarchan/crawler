import urllib.request
import urllib.parse

post_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'

city = input('请输入要查询的城市:')
page = input('请输入要查询第几页:')
size = input('请输入要多少个:')
formdata = {
    'cname': city,
    'pid': '',
    'pageIndex': page,
    'pageSize': size,
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
}

request = urllib.request.Request(url=post_url, headers=headers)
formdata = urllib.parse.urlencode(formdata).encode()

response = urllib.request.urlopen(request, data=formdata)

print(response.read().decode())