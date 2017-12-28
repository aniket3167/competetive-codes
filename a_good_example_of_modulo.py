mod = 10**9+7
def add(x,y):
	x += y 
	if x>mod:
		x-mod
	return x

def mul(x,y):
	return (x*y)%mod
	
def update(x,y):
	while x<=n:
		#print t 
		bit[x] = (bit[x]+y)
		if bit[x] > mod:
			bit[x] -= mod
		x += x&-x
def query(x):
	su = 0
	while x > 0:
		su += bit[x]
		x -= x&-x
	return su%mod
	
f = open('input10.txt' ,'r')
frt = open('anss10.txt','a')
for x in xrange(1):
	n ,a1,b,q = map(int,f.readline().split())
	a = map(int,f.readline().split())
	bit = [0]*(n+1)
	coeff = mul(mod-b,pow(a1,mod-2,mod))
	pos = [1]*n
	for x in xrange(1,n):
		pos[x] = mul(pos[x-1],coeff)
	for x in xrange(n):
		update(x+1,mul(a[x],pos[x])+mod)
	for x in xrange(q):
		qt,c,l = map(int,f.readline().split())
		if qt == 1:
			fr = (mod+l-a[c])% mod
			a[c] = l
			update(c+1,mul(fr,pos[c]))
		else:
			fr = (mod +query(l+1) - query(c))%mod
			if fr == 0:
				frt.write('Yes\n')
			else:
				frt.write('No\n')
f.close()
frt.close()
		