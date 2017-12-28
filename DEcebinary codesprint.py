di = dict()
for x in xrange(900000):
	n = x
	s  = 0
	i = 0
	while n != 0:
		t = n%10
		n = n/10
		s += t*pow(2,i)
		i += 1
	temp = di.get(s,list())
	temp.append(x)
	di[s] = temp
li = []
for x in di.keys():
	di[x].sort()
	li.extend()
for x in xrange(q):
	n = input()
	print li[n-1]