def searchs(seq, number, low = 0, up = None):
	if up is None: up = len(seq) -1
	if low == up:
		number = seq[up]
		return up
	else:
		middle = (low + up)// 2
		if seq[middle] < number:
			return searchs(seq, number, middle + 1, up)
		else:
			return searchs(seq, number, low, middle)




#seq = [34, 67, 8, 123, 4, 100, 95]
#seq.sort()
seq = range(100)
#print searchs(seq, 100)
print seq.index(100)