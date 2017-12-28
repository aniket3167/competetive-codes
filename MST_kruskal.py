from collections import defaultdict

def root( x):
	global root_id
	while(root_id[x] != x):
		root_id[x] = root_id[root_id[x]]
		x = root_id[x]
	return x

def union(x,y):
	global root_id
	p = root(x)
	q = root(y)
	root_id[p] = root_id[q]

def kruskal(graph):
	minimumCost = 0
	global m
	for edge in xrange(m):
		x = graph[edge][0]
		y = graph[edge][1]
		cost = graph[edge][2]
		if root(x) != root(y):
			minimumCost += cost
			union(x,y)
	return minimumCost
	
for x in xrange(input()):
	n,m= map(int,raw_input().split())
	graph = []
	root_id = [x for x in xrange(n)]
	
	total_weight  = 0
	for y in xrange(m):
		sou,end,weight = map(int,raw_input().split())
		total_weight += weight
		graph.append([sou-1,end-1,weight])
	graph.sort(key = lambda value:value[2])
	minimumCost = kruskal(graph)
	print total_weight - minimumCost
	