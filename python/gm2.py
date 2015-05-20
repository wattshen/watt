#!/usr/bin/env python
#coding: utf-8 
#Author: Wattshen
#Email:34665115@qq.com
#Date:
#Filename: 
#Content:

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