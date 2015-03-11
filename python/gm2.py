#!/usr/bin/env python
#coding=gbk
#coding=utf-8
#-*- coding: UTF-8 -*- 

import os,os.path
import shutil,string
 
dir = 'e:\\test'
for i in os.listdir(dir):
    newfile = i.replace('_txt','.txt')
    oldfullfile = dir+'\\'+i
    newfullfile = dir+'\\'+newfile
    print 'this is i:           %s'%i
    print 'this is old name:    %s'%oldfullfile
    print 'this is new name:    %s'%newfullfile
    shutil.move(oldfullfile,newfullfile)
    print 'the next...\n'