# -*- coding: utf-8 -*-
"""
Created on Wed Sep 06 17:47:11 2017

@author: gh

"""
##HTML如何提取关键字

from bs4 import BeautifulSoup   #导入bs4库
import urllib2   # 网络访问模块

#设置代理
enable_proxy = True
proxy_handler = urllib2.ProxyHandler({"http" : 'http://some-proxy.com:8080'})
null_proxy_handler = urllib2.ProxyHandler({})
if enable_proxy:
    opener = urllib2.build_opener(proxy_handler)
else:
    opener = urllib2.build_opener(null_proxy_handler)
urllib2.install_opener(opener)


#发送请求
request = urllib2.Request("https://news.ycombinator.com/newest")
#print response.read()

try:
    response = urllib2.urlopen(request)
except urllib2.HTTPError, e:
    print e.code
except urllib2.URLError, e:
    print e.reason
else:
    print "OK"

soup = BeautifulSoup(response.read())
#print soup.prettify()    #格式化输出
                    
def has_class_and_href(tag):
    return tag.has_attr('class') and tag.has_attr('href')and tag.has_attr('rel')

FindAll = soup.find_all(has_class_and_href)
for amm in FindAll:                                
    print amm   
                    

'''
for i in items:
    itemsFirst = i.find_all(re.compile(r'two moons'))
    
for j in itemsFirst:
    print j    
'''

