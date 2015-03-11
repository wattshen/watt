

f = open(r'e:\test\123.txt','r')
for line in f:
	print line

import sys
text = sys.stdin.read()
words = text.split()
wordcount = len(words)
print 'wordcount',wordcount