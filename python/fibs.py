#!/usr/bin/env python
#coding: utf-8 
#Author: Wattshen
#Email:34665115@qq.com
#Date:
#Filename: 
#Content:

# fibs by function(for)
num = int(raw_input("please input a number, I'll given you a fibs ..."))

def fibs(num):
    result = [0,1]
    for i in range(num-2):
        result.append(result[-2] + result[-1])
	
	#print result
    return result
print fibs(num)

# fibs by class
print 'The topper is function.\nThe bellow is class'
class Fibs():
	def __init__(self):
		self.a,self.b = 0,1
	def next(self):
		self.a, self.b = self.b, self.a + self.b
		'''if self.a > 20:
			raise StopIteration'''
		return self.a
	def __iter__(self):
		return self
fb=Fibs()
xb = []
for i in fb:
	xb.append(i)
	if len(xb) == 11:
		print xb

'''
def x():
	for i in fb:
		if i > 10:
			return
		else:
			yield i
print list(x())

'''