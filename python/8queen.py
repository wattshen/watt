#!/usr/bin/env python
#coding: utf-8 
#Author: Wattshen
#Email:34665115@qq.com
#Date:
#Filename: 
#Content:


state[0] = 1
def confilct (state, nextX):
	nextY = len(state)
	for i in range(nextY):
		if abs(state[i]-nextX) in (0, nextY-i):
			return True
		return False

