#!/usr/bin/env python
#coding: utf-8 
#Author: Wattshen
#Email:34665115@qq.com
#Date:
#Filename: 
#Content:

def checkIndex(key):
	"""
	if the key is right?
	"""
	if not isinstance(key,(int,long)): raise TypeError
	if key<0: raise IndexError


__metaclass__=type # supper only in new python
class xulie():
	def __init__(self, start=0, step=1):
		self.start = start
		self.step = step
		self.changed = {}
	def __getitem__(self, key):
		checkIndex(key)
		try:return self.changed[key]
		except KeyError:
			return self.start+key*self.step
	def __setitem__(self, key, value):
		checkIndex(key)
		self.changed[key] = value
s = xulie()## value is given to __init__, so, __init__ is not space 
s[5] = 100

print 's[4]='+ str(s[4]) + '        s[5]='+ str(s[5])