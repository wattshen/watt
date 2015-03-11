from pprint import pprint
from random import shuffle

# pai
value = range(11) + 'Jack Queen King'.split()

# hua se
suit = 'Red Black Fang Mei'.split()

# pei dui
deck = ['%s of %s'%(v, s) for v in value for s in suit]
shuffle(deck)
pprint(deck[:12])

# xun huan
while deck:
	raw_input(deck.pop())
	if not deck:
		print 'the before is end, the bellow is next'
		deck = ['%s of %s'%(v, s) for v in value for s in suit]
		shuffle(deck)



