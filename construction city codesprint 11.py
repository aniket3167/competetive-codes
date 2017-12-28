#!/bin/python

import sys
from collections import deque

def strongly_connected_components_iterative(vertices, edges):
    """
    This is a non-recursive version of strongly_connected_components_path.
    See the docstring of that function for more details.

    Examples
    --------
    Example from Gabow's paper [1]_.

    >>> vertices = [1, 2, 3, 4, 5, 6]
    >>> edges = {1: [2, 3], 2: [3, 4], 3: [], 4: [3, 5], 5: [2, 6], 6: [3, 4]}
    >>> for scc in strongly_connected_components_iterative(vertices, edges):
    ...     print(scc)
    ...
    set([3])
    set([2, 4, 5, 6])
    set([1])

    Example from Tarjan's paper [2]_.

    >>> vertices = [1, 2, 3, 4, 5, 6, 7, 8]
    >>> edges = {1: [2], 2: [3, 8], 3: [4, 7], 4: [5],
    ...          5: [3, 6], 6: [], 7: [4, 6], 8: [1, 7]}
    >>> for scc in  strongly_connected_components_iterative(vertices, edges):
    ...     print(scc)
    ...
    set([6])
    set([3, 4, 5, 7])
    set([8, 1, 2])

    """
    identified = set()
    stack = []
    index = {}
    boundaries = []

    for v in vertices:
        if v not in index:
            to_do = [('VISIT', v)]
            while to_do:
                operation_type, v = to_do.pop()
                if operation_type == 'VISIT':
                    index[v] = len(stack)
                    stack.append(v)
                    boundaries.append(index[v])
                    to_do.append(('POSTVISIT', v))
                    # We reverse to keep the search order identical to that of
                    # the recursive code;  the reversal is not necessary for
                    # correctness, and can be omitted.
                    to_do.extend(
                        reversed([('VISITEDGE', w) for w in edges[v]]))
                elif operation_type == 'VISITEDGE':
                    if v not in index:
                        to_do.append(('VISIT', v))
                    elif v not in identified:
                        while index[v] < boundaries[-1]:
                            boundaries.pop()
                else:
                    # operation_type == 'POSTVISIT'
                    if boundaries[-1] == index[v]:
                        boundaries.pop()
                        scc = set(stack[index[v]:])
                        del stack[index[v]:]
                        identified.update(scc)
                        yield scc
                        

def kahn_topsort(graph):
    in_degree = { u : 0 for u in graph }     # determine in-degree 
    for u in graph:                          # of each node
        for v in graph[u]:
            in_degree[v] += 1
 
    Q = deque()                 # collect nodes with zero in-degree
    for u in in_degree:
        if in_degree[u] == 0:
            Q.appendleft(u)
 
    L = []     # list for order of nodes
     
    while Q:                
        u = Q.pop()          # choose node of zero in-degree
        L.append(u)          # and 'remove' it from graph
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                Q.appendleft(v)
 
    if len(L) == len(graph):
        return L
    else:                    # if there is a cycle,  
        return []            # then return an empty list

n, m = raw_input().strip().split(' ')
n, m = [int(n), int(m)]

G = {}
par = {}
for a0 in xrange(m):
    u, v = raw_input().strip().split(' ')
    u, v = [int(u), int(v)]
    if v in par:
        par[v].append(u)
    else:
        par[v] = [u]
    if u in G:
        G[u].append(v)
    else:
        G[u] = [v]
    
qsave = []
q = int(raw_input().strip())
for a0 in xrange(q):
    d, x, y = raw_input().strip().split(' ')
    d, x, y = [int(d),int(x), int(y)]
    if d == 1:
        n += 1
        if y == 0:
            if x in G:
                G[x].append(n)
            else:
                G[x] = [n]
            par[n] = [x]
        else:
            G[n] = [x]
            if x in par:
                par[x].append(n)
            else:
                par[x] = [n]
    else:
        qsave.append([x,y])

vert = range(1,n+1)

reach = [set([]) for i in range(n+1)]
for i in range(1,n+1):
    if not i in G:
        G[i] = []
sinnvoll = [0 for i in range(n+1)]

ind = 0
for x in strongly_connected_components_iterative(vert, G):
    ind += 1
    for ex in x:
        sinnvoll[ex] = ind


ng = [set([]) for i in range(ind+1)]
par = [set([]) for i in range(ind+1)]
for i in range(1,n+1):
    for nb in G[i]:
        ng[sinnvoll[i]].add(sinnvoll[nb])
        par[sinnvoll[nb]].add(sinnvoll[i])
ngreach = [set([]) for i in range(ind+1)]
try:
    for i in range(1,ind+1):
        for nod in par[i]:
            ngreach[nod] |= ngreach[i]
            ngreach[nod].add(i)
    for q2 in qsave:
        if (sinnvoll[q2[1]] in ngreach[sinnvoll[q2[0]]]) or (sinnvoll[q2[1]] == sinnvoll[q2[0]]):
            print 'Yes'
        else:
            print 'No'
except:
    for q2 in qsave:
        if sinnvoll[q2[1]] <= sinnvoll[q2[0]]:
            print 'Yes'
        else:
            print 'No'