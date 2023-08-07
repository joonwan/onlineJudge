import sys
input =sys.stdin.readline
sys.setrecursionlimit(int(1e7))

def dfs(now):
    
    global count
    order[now] = count 
    count += 1
    visited[now] = True
    
    for v in graph[now]:
        if not visited[v]:
            dfs(v)

n,m,r = map(int,input().split())

order = [0 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1,n+1):
    graph[i].sort()
count = 1
visited = [False]*(n+1)
dfs(r)

for i in range(1,n+1):
    print(order[i])