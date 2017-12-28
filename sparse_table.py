def build(n):#n : size of array
	for i in xrange(n):
		table[i][0] = arr[i]
	for j in xrange(k+1):
		for i in xrange(n-(1<<j)+1):
			table[i][j] = min(table[i][j-1],table[i+(1<<(j-1))][j-1]
	
#k = int(ceil(log(n)/log(2)))
def query(q):
	for i in xrange(q):
		L,R = map(int,raw_input().split())
		ans = 0
		for j in xrange(k,-1,-1):
			if (L+(1<<j) - 1 <= R):
				answer = min(answer,table[L][j])
				L += 1<<j
		print ans
#instead of min we can use any other function