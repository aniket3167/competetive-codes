/*
 *  Time Complexity - O(V+E) 
*/
#define MAX 100000

list<int> adj[MAX];
bool vis[MAX];

void dfs(int src)
{
	vis[src] = true;
	list<int>::iterator i;
	for(i=adj[src].begin(); i!=adj[src].end(); i++)
	{
		if(!vis[(*i)])
			dfs(*i);
	}
}
