n = input()
s = raw_input()
dp = [[0 for x in xrange(8)] for y in xrange(n)]
dp[0][int(s[0])%8]  = 1;
mod = (10**9)+7
for x in xrange(1,n):
	dp[x][int(s[x])%8] = 1
	for y in xrange(8):
		dp[x][(y*10+int(s[x]))%8] = (dp[x][(y*10+int(s[x]))%8]+dp[x-1][y])%mod
		dp[x][y] = (dp[x][y]  + dp[x-1][y])%mod
print dp[n-1][0]