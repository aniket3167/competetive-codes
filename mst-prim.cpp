#include <bits/stdc++.h>
using namespace std;

int MAX = 1e5 + 5;
#define pii pair<long long, int>
bool mar[MAX];
vector<pii> adj[MAX];

long long prim(int x)
{
	priority_queue<pii, vector<pii> , greater<pii> > Q;
	int y;
	long long mincost = 0;
	pii p;
	Q.push(make_pair(0, x));
	while(!Q.empty()){
		// Selecting the edge with min wt
		p = Q.top();
		Q.pop();
		x = p.second;
		// Checking for cycle
		if(mar[x] == true)
			continue;
		mincost += p.first;
		mar[x] = true;
		for(int i=0; i<adj[x].size(); i++){
			y = adj[x][i].second;
			if(mar[y] == false)
				Q.push(adj[x][i]);
		}
	}
	return mincost;
}

int main()
{
	int nodes, edges, x, y;
    long long weight, minimumCost;
    cin >> nodes >> edges;
    for(int i = 0;i < edges;++i)
    {
        cin >> x >> y >> weight;
        adj[x].push_back(make_pair(weight, y));
        adj[y].push_back(make_pair(weight, x));
    }
    // Selecting 1 as the starting node
    minimumCost = prim(1);
    cout << minimumCost << endl;
    return 0;
	return 0;
}
