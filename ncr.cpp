#define ll long long

inline ll ncr(long n ,long r)
{
	vector<vector<long> > dp(2,vector<long>(r+1,0));
	for(int i=1; i<=n; i++)
	{
		for(int j=0; j<=min(i,r); j++) 
			dp[i&1][j] = ((i==j || j==0)?1:(dp[(i-1)&1][j] + dp[(i-1)&1][j-1])%MOD);
	 }
	 return dp[n&1][r]; 
}

//////			SECOND IMPLEMENTATION				///////

inline ll ncr2(long n, long r) 
{
	ll ans=1; 
	for(long i = n;i>r;i--) 
		ans = (ans*i)%MOD; 
	for(int i=1; i<=n-r; i++) 
		ans = (ans*(modexp(i,MOD-2,MOD)))%MOD;
		
	return ans; 
}
