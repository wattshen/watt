#!/usr/bin/env python
#coding: utf-8 
#Author: Wattshen
#Date:
#Filename: 
#Content:

import cmath
print cmath.sqrt(-10)
print pow(2,3,5)
#name = raw_input('your name...')
#print 'your name is', name
#help()
#raw_input('press <enter>')

print 'wei_di_gui_jie_c'
def wei(n,a=1):
	if n == 1:
		return a
	else:
		return wei(n-1, a*n)

print wei(1000)

