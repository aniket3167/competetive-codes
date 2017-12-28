a,b = map(int,raw_input().split())
bi = bin(b)[2:]
t  = len(bi)
ans = a
cnt = 1
for x in xrange(1,t):
	ans = ans* ans
	cnt += 1
	if bi[x] == '1':
		cnt += 1
		ans = ans *a
print 'x^y is equal to ' , ans
print 'number of iterations is equal to ',cnt