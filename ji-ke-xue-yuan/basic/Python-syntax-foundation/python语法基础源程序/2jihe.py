#!/usr/bin/env python
#coding: utf-8
#-*-*-  Author: Wattshen       -*-*-
#-*-*-  Email:34665115@qq.com  -*-*-
#-*-*-  Filename:.py  -*-*-
#-*-*-  Date:
#Content:

a=set("abcnmmmmaaaaggsng")
b=set("cdfm")
#交集
x=a&b

#并集
y=a|b

#差集
z=a-b

#去除重复元素
new=set(z)
print new
