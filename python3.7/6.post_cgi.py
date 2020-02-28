# encoding:utf-8
import random
import urllib.request
import urllib.parse

data = {"obs_year": "2011", "obs_month": "March", "obs_day": "22"}
params = "?"
for key in data:
    params = params + key + "=" + data[key] + "&"
data = urllib.parse.urlencode(data).encode('utf-8')
url = "https://umbra.nascom.nasa.gov/cgi-bin/eit-catalog.cgi"
request = urllib.request.Request(url, data)#
page = urllib.request.urlopen(request).read()
page = page.decode('utf-8')
print(page)