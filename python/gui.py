#! /usr/bin/python

#filename:hello.py

i = 0
while i < 50:
	i += 1
	if i % 4 <>0:
		continue
	if i + 76 ==100:
		break
	print i


def shusu(a, b):
	for x in range(a, b+1):
		if x%2==0:
			continue
		elif x > b:
			break
		else:
			print x
shusu(999,1011)

help()
raw_input ('please type <enter>')