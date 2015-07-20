#!/usr/bin/env python
#coding: utf-8 
#Author: Wattshen
#Email:34665115@qq.com
#Filename: .py
#Date:2015-3-14
#Content:
<<<<<<< HEAD

=======
>>>>>>> master
#随机猜数游戏
#使用了随机数生成
#使用了三种不同的文本打印策略
#通过循环实现，并按用户输入内容给出提示

import random
name = 'tom'
number = random.choice(range(100))
guess = ''
times = 0
while guess != number:#表达式中不可以出现语句不能写成while guess = int(raw_input('Enter an integer : ')) != number 
	guess = int(raw_input('Enter an integer : '))
	times += 1
	if guess < number:
		print "it's too small, please type a big one..."
	elif guess > number:
		print "it's too big, please type a small one..."
else:
	format = ('hello,%s! you guessed it with %s, it is %s')
	values = (name, times,guess)
	print format % values  # frist
	print 'hello ' + name + '! Congratulations, you guessed it, it is ' + str(guess) +'.'# second
	print 'hello %s! Congratulations, you guessed it, it is %s.' % (name,guess) # third
print 'Done'