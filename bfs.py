def bfs(graph, source, target):
    queue = []
    visited = {}
    parent = {}
    
    for node in xrange(len(graph)):
        visited[node] = False
        parent[node] = None
    
    queue.append(source)
    while len(queue) != 0:
        current = queue.pop(0)
        if current == target:
            print backtrace(parent, source, target)
            break
        for neighbor in graph[current]:
            if visited[neighbor] == False:
            	visited[neighbor] = True
                parent[neighbor] = current
            	queue.append(neighbor)