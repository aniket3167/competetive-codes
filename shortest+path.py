from heapq import *
from collections import *
def dij(x):
	global visited
	dis = [10000000 for ti in xrange(node)]
	dis[x] = 0
	heap = []
	heappush(heap,[0,x])
	while heap:
		p = heappop(heap)
		x = p[1]
		if visited[x] == 1:
			continue
		distance = p[0]
		dis[x] = distance
		visited[x] = 1
		for i in graph[x]:
			y = i[0]
			if visited[y] == 0:
				if distance + i[1]<dis[y]:
					heappush(heap,[i[1]+distance,i[0]])
		#print heap
	return dis
				

for x in xrange(input()):
	node,edge = map(int,raw_input().split())
	graph = defaultdict(list)
	visited = [0]*node
	for y in xrange(node):
		graph[y] = []
	for y in xrange(edge):
		sou,end,weight = map(int,raw_input().split())
		graph[sou-1].append([end-1,weight])
		graph[end-1].append([sou-1,weight])
	#print graph
	s = int(raw_input())
	distan = dij(s-1)
	for l in xrange(len(distan)):
		if l != s-1:
			if distan[l] == 10000000:
				print -1,
			else:
				print distan[l],
		'''elif distan[l] != 10000000:
			print -1,'''
	print 
		