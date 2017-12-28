from math import *
def dfs(cur,prev):
	#print cur,prev
	depth[cur] = depth[prev] + 1
	parent[cur][0] = prev
	stack = []
	stack.append(cur)
	while len(stack) != 0:
		cur = stack.pop()
		prev = parent[cur][0]
		for i in xrange(len(graph[cur])):
			if graph[cur][i] != prev:
				stack.append(graph[cur][i])
				parent[graph[cur][i]][0] = cur
				depth[graph[cur][i]] = depth[cur] + 1

def precomputeSparseMatrix(n):#n : size of tree
	for i in xrange(1,level):#level = int(ceil(log(n)/log(2)))
		for node in xrange(1,n+1):
			if parent[node][i-1] != -1:
				parent[node][i] = parent[parent[node][i-1]][i-1]

def lca(u,v):
	if depth[v] < depth[u]:
		u,v = v,u
	diff = depth[v] - depth[u]
	for i in xrange(level):
		if ((diff>>i)&1) == 1:
			v = parent[v][i]
	if u == v:
		return u
	for i in xrange(level - 1,-1,-1):
		if parent[u][i] != parent[v][i]:
			u = parent[u][i]
			v = parent[v][i]
	return parent[u][0]
	

node = input()
#tree node starts from 1
depth = [0]*(node+1)
level = int(ceil(log(node)/log(2)))
parent = [[-1 for x in xrange(level)] for y in xrange(node+1)]
graph = dict()
for y in xrange(node):
	graph[y+1] = []
for y in xrange(node-1):
	sou,end,weigt = map(int,raw_input().split())
	tmp = graph.get(sou,list())
	tmp.append(end)
	graph[sou] = tmp
	end ,sou = sou,end
	tmp = graph.get(sou,list())
	tmp.append(end)
	graph[sou] = tmp
dfs(1,0)
precomputeSparseMatrix(node)
print lca(2,3)