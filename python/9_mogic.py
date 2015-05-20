#!/usr/bin/env python
#coding: utf-8 
#Author: Wattshen
#Email:34665115@qq.com
#Date:
#Filename: 
#Content:

class Foobar:
	def __init__(self):
		self.somevar = 42
		print self.somevar
f = Foobar()
# f.somevar

class Foobar2:
	def __init__(self, value = 100):
		self.somevar = value
		print self.somevar
f2 = Foobar2('i love you, python')
# f2.somevar

#static method and class method
__metaclass__ = type
class Myclass:
#	@staticmethod
	def smeth():
		print 'This is a static method.'
	smeth = staticmethod(smeth) 
#	@classmethod
	def cmeth(cls):
		print 'this is a class method of', cls
	cmeth = classmethod(cmeth)
Myclass.smeth()
Myclass.cmeth()

nested = [[1,2],[3,4],[5,6]]
myvar = [[1, 2], [3, [100, 101, 102,[103, 104,[105, [106,[107,108]]]]], 4], [5, 6]]

############
print 'flatten3 start'

def flatten3(x):
	for sublist in x:
		if isinstance(sublist, list):
			for element in flatten3(sublist):
				yield element
		else:
			yield sublist

for num in flatten3(nested):
	print num


print 'flatten3 end'

####


def flatten(nested):
	for sublist in nested:
			for element in sublist:

				yield element
for num in flatten(nested):
	print num

######


def flatten2(nested):
	x = []
	for sublist in nested:
		for element in sublist:
			x.append(element)
			#print element
	return x
	#return sublist

print(flatten2(nested))
