from collections import *

def dfs_cycle(adjLists, visited, v):
	visited[v] = True
	global stack
	if v in stack:
		return 1
	stack.append(v)
	for w in adjLists[v]:
	dfs_rec(adjLists, visited, w[0])
		stack.pop()
	return 0
for x in xrange(input()):
	n,m = map(int,raw_input().split())
	graph = defaultdict(list)
	visited = [0]*n
	stack  = []
	for y in xrange(node):
		graph[y] = []
	for y in xrange(m):
		sou,end,weight = map(int,raw_input().split())
		graph[sou-1].append([end-1,weight])
	is_cycle = dfs_cycle(graph,visited,0)
	if is_cycle:
		print 'Cycle'
	else:
		print 'No Cycle' 
	