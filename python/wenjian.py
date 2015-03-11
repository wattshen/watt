#!/usr/bin/env python
#coding=gbk
#coding=utf-8
#-*- coding: UTF-8 -*- 

#打开本地文件,注意权限
f = open(r'e:\test\123.txt','a')
#写入文件,注意换行
f.write('hello, this is my frist code of file.\r\n')
f.read

import fileinput
print fileinput.filename('e:\test\123.txt')
fileinput.nextfile()
f.close()
