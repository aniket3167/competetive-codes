# recursive DFS version
def dfs_rec(adjLists, visited, v):
	visited[v] = True
	
	for w in adjLists[v]:
		n = len(adjLists[v])
		if(not visited[w]):
			dfs_rec(adjLists, visited, w)
			cnt[v] += cnt + 1.0/n
 cnt = [0]*n