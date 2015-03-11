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