from collections import *
def bfs(sou):
    global graph
    global visit
    visit[sou-1] = 1
    n = 1
    que = deque()
    que.append(sou)
    while que:
        x1 = que.popleft()
        for x2 in graph[x1]:
            if visit[x2-1] != 1:
                que.append(x2)
                visit[x2-1] = 1
                n += 1
    return n
    
    
for x in xrange(input()):
    n,m,lib,road = map(int,raw_input().split())
    visit = [0]*n
    graph = dict()
    cost = 0
    if m == 0:
        print n*lib
        continue
    for y in xrange(n):
		graph[y+1] = []
    for y in xrange(m):
		sou,end = map(int,raw_input().split())
		tmp = graph.get(sou,list())
		tmp.append(end)
		graph[sou] = tmp
		end ,sou = sou,end
		tmp = graph.get(sou,list())
		tmp.append(end)
		graph[sou] = tmp
    for x1 in xrange(n):
        if visit[x1] == 0:
            n = bfs(x1+1)
            if lib < road:
                cost = cost + n*lib
            else:
                cost += lib + (n-1)*road
    print cost