from math import *
def eratosthenes2(n):
    multiples = set()
    for i in range(2, n+1):
        if i not in multiples:
            yield i
            multiples.update(range(i*i, n+1, i))
 
#print(list(eratosthenes2(100)))

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
def eular(n):
	result = n
	prime = primes(n)
	#print prime ,'prime',n
	for x in prime.keys():
		result -= result/(x)
	return result
for x in xrange(10):
	print eular(x+1)
			