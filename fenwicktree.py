def update(x,y):
	while x<=n:
		#print t 
		bit[x] += y
		x += x&-x
def query(x):
	su = 0
	while x > 0:
		su += bit[x]
		x -= x&-x
	return su
for x in xrange(input()):
	n = input()
	a = map(int,raw_input().split())
	bit = [0]*(n+1)
	for x in xrange(1,n+1):
		update(x,a[x-1])
	print bit
	print query(6)
		