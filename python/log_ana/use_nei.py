#!/usr/bin/env python
#coding: utf-8 
#-*-*-  Author: Wattshen       -*-*-
#-*-*-  Email:34665115@qq.com  -*-*-
#-*-*-  Filename:use_nei.py  -*-*-
#-*-*-  Date:  

import datetime
#import n_juhe
from n_juhe import juhe

'''
	直接import时,模块名　类名　方法名可以直接用　
	以from modle_name import class_name导入时，需以　类名.方法名　　来用
'''
start_time = datetime.datetime.now()

f = open(r'G:\watt\python\log_ana\20150707.csv','r+')
jh = juhe()
lines = jh.split_line(f)

print "以下分别是文件中的唯一电话、关键词、ＳＩＤ："
F_MOBILE = jh.cut(lines, 'F_MOBILE')
F_KEYWORD = jh.cut(lines, 'F_KEYWORD')
SESSION_ID = jh.cut(lines, 'SESSION_ID')
F_DATE = jh.cut(lines, 'F_DATE')
F_TIME = jh.cut(lines, 'F_TIME')
print "---------------------------------------------------------\n\n\n以下分别是具体的ＳＩＤ、电话在原文件中出现的位置："

p = jh.he(lines, SESSION_ID, 'SESSION_ID')

#jh.he(lines, F_MOBILE, 'F_MOBILE')


print '---------------------------------------------------------\n\n\n格式输出：'
jh.ord_sid(p,lines)















end_time = datetime.datetime.now()
print "\n\n---------------------------------------------------------\n本次处理开始于%s，结束于%s" % (start_time, end_time)


