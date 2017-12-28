from collections import defaultdict
from heapq import *

def prim(x):
	global visited
	heap = []
	minimumCost = 0
	heappush(heap,[0,x])
	while heap:
		p = heappop(heap)
		#print p
		x = p[1]
		if visited[x] == 1:
			continue
		minimumCost += p[0]
		visited[x] = 1
		for i in graph[x]:
			y = i[0]
			if visited[y] == 0:
				heappush(heap,[i[1],i[0]])
	return minimumCost
for x in xrange(1):
	node,edge  = map(int,raw_input().split())
	graph = defaultdict(list)
	total = 0
	visited = [0]*node
	for y in xrange(node):
		graph[y] = []
	for y in xrange(edge):
		sou,end,weight = map(int,raw_input().split())
		total += weight
		graph[sou-1].append([end-1,weight])
		graph[end-1].append([sou-1,weight])
	#print graph
	minimumCost = prim(0)
	print total-minimumCost