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
#���������Ϸ
#ʹ�������������
#ʹ�������ֲ�ͬ���ı���ӡ����
#ͨ��ѭ��ʵ�֣������û��������ݸ�����ʾ

import random
name = 'tom'
number = random.choice(range(100))
guess = ''
times = 0
while guess != number:#���ʽ�в����Գ�����䲻��д��while guess = int(raw_input('Enter an integer : ')) != number 
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