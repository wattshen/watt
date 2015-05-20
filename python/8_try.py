#!/usr/bin/env python
#coding: utf-8 
#Author: Wattshen
#Email:34665115@qq.com
#Date:
#Filename: 
#Content:


def divi():
	while True: 
		try:
			x = input('the frist number:')
			y = input('the second number:')
			print x/y
		except ZeroDivisionError:
			print "the second number can't be zero"
		else:
			break
divi()