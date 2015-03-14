#!/usr/bin/env python
#coding: utf-8 
#Author: Wattshen
#Filename: shen.py
#Date:2015-3-14
#Content:


print '加上一行#coding: utf-8 就可以输出中文！'
def xunh(n):
	i=result= 1
	#result = n
	#i = 1
	while i <= n:
		result *= i
		i += 1
	return result

print xunh(5)



def forh(n):
	result = n
	for i in range(1, n):
		result *= i
	return result
print forh(5)


def diedai(n):
	if n == 1: return 1
	else:
		result = n * diedai(n-1)
		return result
print diedai(5)


def power_d(x,n):
	if n == 0: return 1
	else:
		x *= power_d(x,n-1)
		return x
print power_d(3,2)


def searchs(seqs, number, lower, upper):
	if lower == upper:
		assert number == seqs[upper]
		return upper
	else:
		middle = (lower + upper) // 2
		if number > middle:
			return searchs(seqs,number,middle+1, upper)
		else:
			return searchs(seqs,number,lower,middle)
x = range(100)
searchs(x,34)







