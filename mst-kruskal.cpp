#include <bits/stdc++.h>
using namespace std;

int MAX = 1e5 + 5;
int id[MAX], node, edges;

pair <long long, pair<int, int> > p[MAX];

void initialize()
{
	for(int i=0; i<MAX; i++)
		id[i] = i;
}

int dad(int x)
{
	while(id[x] != x){
		id[x] = id[id[x]];
		x = id[x];
	}
	return x;
}

void union1(int x, int y)
{
	int p = dad(x);
	int q = dad(y);
	
	id[p] = id[q];
}

long long kruskal(pair<long long, pair<int, int> > p[])
{
	int x,y;
	long long cost, mincost = 0;
	
	for(int i=0; i<edges; i++){
		// Selecting edges one by one in increasing order from the begining
		x = p[i].second.first;
		y = p[i].second.second;
		
		// Check if the selected edge is creating a cycle or not
		if(dad[x] != dad[y]){
			mincost += cost;
			union1(x, y);
		}
	}
	return mincost;
}

int main()
{
	int x,y;
	long long wt, cost, mincost;
	initialize();
	cin>>nodes>>edges;
	
	for(int i=0; i<edges; i++){
		cin>>x>>y>>wt;
		p[i] = make_pair(wt, make_pair(x,y));
	}
	
	// Sort the edges in ascending order
	sort(p, p+edges);
	mincost = kruskal(p);
	cout<<mincost<<endl;
	return 0;
}
