#알고리즘 수업 - 깊이 우선 탐색

import sys
input = sys.stdin.readline


def dfs(now):
    global count
    visited[now] = True
    order[now] = count
    count += 1
    
    for v in graph[now]:
        if not visited[v]:
            dfs(v)
n,m,r = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
for _ in range(m):
    
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1,n+1):
    graph[i].sort(reverse=True)

order = [0 for _ in range(n+1)]
count = 1
dfs(r)

for i in range(1,n+1):
    print(order[i])