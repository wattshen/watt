class My_e(Exception):
	print 'this is my frist Exception'
while True:
	try:
		x = int(raw_input('enter the frist number:'))
		y = int(raw_input('enter the second number:'))
		value = x / y
		print 'x/y is',value
	except Exception, e:
		print 'invalid input:',e
		print 'please try again'
	else:
		raise TypeError
		break


