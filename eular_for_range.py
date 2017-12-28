def divis(n = 500000):
	#eular_for_range
	phi = [x for x in xrange(n+1)]
	div = [0]*(n+1)
	for x in xrange(2,n+1):
		if phi[x] == x:
			phi[x] = x-1
			for y in xrange(2*x,n+1,x):
				phi[y] -= phi[y]/x
	#print phi[:9]
	#sum of divisiors
	for x in xrange(1,n+1):
		for y in xrange(x,n+1,x):
			div[y] += phi[x]
		
	#print div[:9]
	return div