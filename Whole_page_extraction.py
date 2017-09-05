# -*- coding: utf-8 -*-
"""
Created on Tue Sep 05 20:40:45 2017

@author: gh
"""
import urllib2

#设置代理
enable_proxy = True
proxy_handler = urllib2.ProxyHandler({"http" : 'http://some-proxy.com:8080'})
null_proxy_handler = urllib2.ProxyHandler({})
if enable_proxy:
    opener = urllib2.build_opener(proxy_handler)
else:
    opener = urllib2.build_opener(null_proxy_handler)
urllib2.install_opener(opener)

#向url发请求，收回复
request = urllib2.Request("https://news.ycombinator.com")
response = urllib2.urlopen(request,timeout = 20)

#将结果打印
print response.read()
