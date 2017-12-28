# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
sys.setrecursionlimit(10**5+30)
def leaf(node):
    if len(graph[node]) == 1 and graph[node] == par[node]:
        return 1
    else:
        return 0
def dfs(sou):
    par[sou] = -1
    stack = [1]
    visited = [0]*(n+1)
    visited[sou] = 1
    while stack:
        w = stack.pop()
        for v in graph[w]:
            if not visited[v]:
                visited[v] = 1
                stack.append(v)
                par[v] = w
def solve(cur,col,steak):
    if dp[cur][col][steak] != -1:
        return dp[cur][col][steak]
    if leaf(cur):
        if steak == 1:
            dp[cur][col][steak] = 0
            return 0
        else:
            dp[cur][col][steak] = 1
            return 1
    ans = 1
    invalid = 1
    for x in graph[cur]:
        if par[cur] != x:
            valid = solve(x,1-col,1)
            invalid = (invalid*valid)%mod
            valid += solve(x,col,2)
            ans = (ans*valid)%mod
    if steak == 1:
        ans = (ans - invalid+mod)%mod
    dp[cur][col][steak] = ans
    return ans


mod = 10**9 + 7
n = input()
m = n - 1
graph = dict()
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
dp = [[[-1,-1,-1] for x in xrange(2)] for y in xrange(n+1)]
par = [0]*(n+1)
#print 1
dfs(1)
#print par
ans = (solve(1,0,1)*2)%mod
print ans
            
            