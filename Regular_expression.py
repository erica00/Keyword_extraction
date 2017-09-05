# -*- coding: utf-8 -*-
"""
Created on Tue Sep 05 22:35:23 2017

@author: gh
"""
#正则表达式

import re

# 使用search()查找匹配的子串，不存在能匹配的子串时将返回None
# 这个例子中使用match()无法成功匹配
patternS = re.compile(r'hello')
match = re.search(patternS,'world hello')
if match:
    # 使用Match获得分组信息
    print match.group()
### 输出 ###
# world
# 将正则表达式编译成Pattern对象，注意hello前面的r的意思是“原生字符串”
else:
    print 'Search匹配失败'
#优先选择search方法




#使用match()查找匹配的子串
pattern = re.compile(r'hello')# 使用re.match匹配文本，获得匹配结果，无法匹配时将返回None
#pattern.match()和re.match(pattern,...)用法相同
result1 = pattern.match('world hello')
result2 = re.match(pattern,'helloo CQC!')
result3 = re.match(pattern,'helo CQC!')
result4 = re.match(pattern,'hello CQC!')
 
#如果1匹配成功
if result1:
    # 使用Match获得分组信息
    print result1.group()
else:
    print '1匹配失败！'
 
#如果2匹配成功
if result2:
    # 使用Match获得分组信息
    print result2.group()
else:
    print '2匹配失败！'
 
#如果3匹配成功
if result3:
    # 使用Match获得分组信息
    print result3.group()
else:
    print '3匹配失败！'
 
#如果4匹配成功
if result4:
    # 使用Match获得分组信息
    print result4.group()
else:
    print '4匹配失败！'
