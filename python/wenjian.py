#!/usr/bin/env python
#coding=gbk
#coding=utf-8
#-*- coding: UTF-8 -*- 

#打开本地文件,注意权限
f = open(r'G:\watt\python\log_ana\122.csv','a=')
#写入文件,注意换行
f.write('hello, this is my frist code of file.\r\n')
f.readline()

import fileinput
print fileinput.filename('e:\test\123.txt')
fileinput.nextfile()
f.close()
