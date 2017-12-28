def update(x,y):
	while x<=n:
		#print t 
		bit[x] += y
		x += x&-x

def range_update(mx,mn,y):
	update(mx,y)
	update(mn+1,-y)

def query(x):
	su = 0
	while x > 0:
		su += bit[x]
		x -= x&-x
	return su+a[x-1]
for x in xrange(input()):
	n = input()
	a = map(int,raw_input().split())
	bit = [0]*(n+1)
	