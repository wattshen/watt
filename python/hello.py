#! /usr/bin/python

#filename:hello.py
'i love you'

name = raw_input\
('''Goodmorning
please enter your name:___''')

print 'my name is:',name


number = 23
guess = int(raw_input('Enter an integer : '))

while guess != number:
	guess = int(raw_input('This time is wrong, enter anther integer:'))
else:
	format = ('hello,%s! Congratulations to you, you guessed it, it is %s')
	values = (name, guess)
	print format % values  # frist
	print 'hello ' + name + '! Congratulations, you guessed it, it is ' + str(guess) +'.'# second
	print 'hello %s! Congratulations, you guessed it, it is %s.' % (name,guess) # third
print 'Done'
# This last statement is always executed, after the if statement is executed 

sum = 0
t = range(100)
for x in t:
	sum = sum + x
print sum

raw_input ('please type <enter>')