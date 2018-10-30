#include <bits/stdc++.h>
using namespace std;

#define pb push_back
#define MAX 100007
vector<int> adj[MAX];
int vis[MAX];

int dfs(int v)
{
	vis[v] = true;
//	cout<<v<<" ";
	int cnt = 1;
	vector<int>::iterator i;
	for(i=adj[v].begin(); i!=adj[v].end(); i++)
	{
		if(!vis[*i])
		{
			cnt += dfs(*i);
		}
	}
	return cnt;
}

int main()
{
	ios::sync_with_stdio(false);	cin.tie(NULL);
	int n,m;	cin>>n>>m;
	while(m--)
	{
		int x,y;	cin>>x>>y;
		x -= 1;
		y -= 1;
		adj[x].pb(y);
		adj[y].pb(x);
	}
	memset(vis, 0, sizeof(vis));
	for(int i=0; i<n; i++)
	{
		if(vis[i] == 0)
		{
			int x = dfs(i);
			cout<<endl;
			cout<<x<<endl;
		}
	}
	return 0;
}
