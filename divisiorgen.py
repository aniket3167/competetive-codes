from math import *
def eratosthenes2(n):
	multiples = set()
	for i in range(2, n+1):
		if i not in multiples:
			yield i
			multiples.update(range(i*i, n+1, i))

def primes(n):
	h = int(sqrt(n)) + 1
	prime  = list(eratosthenes2(h))
	factors = {}
	for x in prime:
		if n == 1:
			break
		while n%x == 0:
			n = n/x
			factors[x] = factors.get(x,0) + 1
	if n != 1:
		factors[n] = 1
	return factors
	
	
def divisorGen(n):
	prime = primes(n)
	factors = [[k,v] for k,v in prime.items()]
	nfactors = len(factors)
	f = [0] * nfactors
	while True:
		yield reduce(lambda x, y: x*y, [factors[x][0]**f[x] for x in range(nfactors)], 1)
		i = 0
		while True:
			f[i] += 1
			if f[i] <= factors[i][1]:
				break
			f[i] = 0
			i += 1
			if i >= nfactors:
				return
print list(divisorGen(102))