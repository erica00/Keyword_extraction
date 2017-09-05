# -*- coding: utf-8 -*-
"""
Created on Tue Sep 05 23:02:08 2017

@author: gh
"""
##HTML如何提取关键字
#导入bs4库
from bs4 import BeautifulSoup
import urllib2
'''
#test html
html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
'''

request = urllib2.Request("https://news.ycombinator.com/newest")
response = urllib2.urlopen(request,timeout = 40)
#print response.read()


soup = BeautifulSoup(response.read())
#print soup.prettify()

'''
#以下方法只能查询第一个符合的内容
print soup.a     #查询a
print soup.a.attrs  #查询a的属性
print soup.a['href']  #查询a中属性‘href的值’
'''
 
#连续查询内容的方法
#'NavigableString'
'''
for child in soup.descendants:
    print child

'''
def has_class_and_href(tag):
    return tag.has_attr('class') and tag.has_attr('href')and tag.has_attr('rel')

FindAll = soup.find_all(has_class_and_href)

'''
for a in FindAll:                                
    print FindAll
'''
