#!/usr/bin/env python
#coding=gbk
#coding=utf-8
#-*- coding: UTF-8 -*- 

#�򿪱����ļ�,ע��Ȩ��
f = open(r'G:\watt\python\log_ana\122.csv','a=')
#д���ļ�,ע�⻻��
f.write('hello, this is my frist code of file.\r\n')
f.readline()

import fileinput
print fileinput.filename('e:\test\123.txt')
fileinput.nextfile()
f.close()
