#!/usr/bin/env python
#coding: utf-8 
#Author: Wattshen
#Email:34665115@qq.com
#Date:
#Filename: 
#Content:

f = open(r'e:\test\123.txt','r')
for line in f:
	print line

import sys
text = sys.stdin.read()
words = text.split()
wordcount = len(words)
print 'wordcount',wordcount