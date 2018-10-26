/**
 * Description: BFS (Checks if graph is connected using BFS)
 * Usgae: isConnected O(V + E) 
 */

int isConnected(vector<vector<int> > &G, int src){
	bool vis[MAX] = {false};
	queue<int> Q;
	Q.push(src);
	while (Q.size()) {
		int u = Q.front();
		Q.pop();
		vis[u] = true;
		for (int v : G[u]) {
			if (!vis[v]) {
				Q.push(v);
			}
		}
	}
	for (int i = 0; i < G.size(); i++) {
       		if (vis[i] == false) {
            		return false;
        	}
	}
	return true;
}
