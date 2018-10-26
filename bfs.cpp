#include <bits/stdc++.h>
using namespace std;

vector<int> adj[100007];
bool vis[100007];

void bfs(int src)
{
	list<int> que;
	vis[src] = true;
	
	que.push_back(src);
	vector<int>::iterator i;
	
	while(!que.empty()){
		src = que.front();
		cout<<src<<" ";
		que.pop_front();
		
		for(i = adj[src].begin(); i != adj[src].end(); ++i){
			if(!vis[*i]){
				vis[*i] = true;
				que.push_back(*i);
			}
		}
	}
}

int main()
{
	int n,m;	cin>>n>>m;
	// for no of nodes and edges
	for(int i=0; i<m; i++){
		int x,y;	cin>>x>>y;
		adj[x].push_back(y);
		adj[y].push_back(x);
	}
	memset(vis, false, sizeof(vis));
	
	cout<<"The bfs traversal of following is \n";
	bfs(1);
	return 0;
}
