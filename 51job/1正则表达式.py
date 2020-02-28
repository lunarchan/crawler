# encoding:utf-8
import re

mystr=""""<div class=\"rt\">
    共30957条职位
</div>"""

restr="(\\d+)"#正则表达式，若带括号，则只返回括号内的东西
regex=re.compile(restr,re.IGNORECASE)
mylist=regex.findall(mystr)
print(mylist[0])