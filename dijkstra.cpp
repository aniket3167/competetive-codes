#include <bits/stdc++.h>
using namespace std;

#define pi pair<int, int>
#define MAX 1000
# define INF 0x3f3f3f3f

int V,m;
list< pair<int, int> > adj[MAX];

void dijkstra(int src)
{
    priority_queue< pi, vector <pi> , greater<pi> > pq;
 
    vector<int> dist(V, INF);
 
    pq.push(make_pair(0, src));
    dist[src] = 0;
    while (!pq.empty())
    {
        int u = pq.top().second;
        pq.pop();
        list< pair<int, int> >::iterator i;
        for (i = adj[u].begin(); i != adj[u].end(); ++i)
        {
            int v = (*i).first;
            int weight = (*i).second;
            if (dist[v] > dist[u] + weight)
            {
                dist[v] = dist[u] + weight;
                pq.push(make_pair(dist[v], v));
            }
        }
    }
    printf("Vertex   Distance from Source\n");
    for (int i = 0; i < V; ++i)
        printf("%d \t\t %d\n", i, dist[i]);
}

int main()
{
	cin>>V>>m;
	// V no of nodes and m no of edges
	
	while(m--){
		int x,y,w;		cin>>x>>y>>w;
		adj[x].push_back(make_pair(y, w));
		adj[y].push_back(make_pair(x, w));
	}
	dijkstra(0);
	return 0;
}
