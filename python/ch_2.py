#!/usr/bin/env python
#coding: utf-8 
#-*-*-  Author: Wattshen       -*-*-
#-*-*-  Email:34665115@qq.com  -*-*-
#-*-*-  Filename:ch_2.py  -*-*-
#-*-*-  Date:2015年3月27日
#Content:list & tuple

x = [1,2,3,4,5]
y = x[:]#y和x是两个变量，只是值相等而已。区别于y=x,（是指向同一个内存地址的两个变量）
y.sort() #原处修改了y，但是返回空
y.reverse()

x[1:1]='iloveyou'#侵害成字母后插入
x[1:1]=['iloveyou']#作为一个完整的字符串插入

y = sorted(x) #sorted是一个函数，将处理结果返回

