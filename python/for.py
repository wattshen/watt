d = {'x':1, 'y':2, 'z':3}
for key in d:
	print key, 'corresponds', d[key]

for a,b in d.items():
	print a,b

print d.values

print [x*y for x in range(10) for y in range(15) if x%3==0 or y%7==0]

q=10 if 'ok' else 'no'
print q
