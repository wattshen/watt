#!/usr/bin/env python
#coding: utf-8 
#Author: Wattshen
#Email:34665115@qq.com
#Date:
#Filename: 
#Content:

#�򿪱����ļ�,ע��Ȩ��
f = open(r'G:\watt\python\log_ana\122.csv','a=')
#д���ļ�,ע�⻻��
f.write('hello, this is my frist code of file.\r\n')
f.readline()

import fileinput
print fileinput.filename('e:\test\123.txt')
fileinput.nextfile()
f.close()
