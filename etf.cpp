#include <cstdio>
#include <set>
using namespace std;
 
set<int> factorize(int n) {
    set<int> facts;
    for (int i = 2; i * i <= n; ++i) {
        while (n % i == 0) {
            facts.insert(i);
            n /= i;
        }
    }
 
    if (n != 1) {
        facts.insert(n);
    }
    return facts;
}
 
int main() {
	int n;
	scanf("%d", &n);
 
	set<int> facts = factorize(n);

	for(int p : facts) {
		n = (n / p) * (p - 1); // since p are divisors of n, n/p is always an integer.
	}

	printf("%d\n", n);
 
	return 0;
}

////////////////////////////////////////////////////////////////////////////////////////////////////////
/* 					ETF # 2							*/
#include <bits/stdc++.h>
using namespace std;

#define MAX 1000007
#define SQ  1007

vector<bool> isprime(MAX+1,true);
int small[MAX+1];
inline void sieve()
{ 
	isprime[0]=isprime[1]=0; 
	int i,j; 
	for(i=4;i<=MAX;i+=2) 
		isprime[i]=0;
	for(i=3;i<=SQ;i+=2) 
		if(isprime[i]) 
			for(j=i*i;j<=MAX;j+=(i+i)) 
				isprime[j]=0;  
}

int main()
{
	int n;	cin>>n;
	sieve();
	long long ans = n;
	for(int i=2; i*i<=n; i++)
	{
		if(isprime[i] && n%i == 0)
		{
			ans = ans/i;
			ans = ans*(i-1);
		}
	}
	cout<<ans<<endl;
	return 0;
}
