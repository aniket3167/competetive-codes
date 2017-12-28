def sub(dp,arr,n,sm,k):
	global ct
	#print sm,'sm' ,n,'n'
	if sm == 0:
		if k == 0:
			ct = ct + 1
		return
	if n == 0 or sm < 0:
		return
	if sm>= arr[n-1]:
		if dp[sm-arr[n-1]][n-1] == 1:
			sub(dp,arr,n-1,sm-arr[n-1],k-1)
	if dp[sm][n-1] == 1:
		sub(dp,arr,n-1,sm,k)
	return
def subset(arr,n,sm,k):
	dp = [[0 for x in xrange(n+1)] for x in xrange(sm+1)]
	dp[0] = [ 1 for x in xrange(n+1)]
	#for x in xrange(sm+1):
	#	print dp[x]
	for x in xrange(1,sm+1):
		for y in xrange(1,n+1):
			dp[x][y] = dp[x][y-1]
	#		print x,'x',arr[y-1],'arrr'
			if x >=arr[y-1]  and dp[x-arr[y-1]][y-1] == 1:
				dp[x][y] = 1
	return sub(dp,arr,n,sm,k)
	#for x in xrange(sm+1):
		#print dp[x]
			
for _ in xrange(input()):
	try:
		n,k,sm = map(int,raw_input().split())
	except:
		n,k,sm = 2 ,1,10
	arr = [y+1 for y in xrange(n)]
	ct = 0    
	subset(arr,n,sm,k)
	print ct
		