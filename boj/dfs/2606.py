## 바이러스

import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e6))

def dfs(now):
    global count
    visited[now] = True
    count += 1
    for v in graph[now]:
        if not visited[v]:
            dfs(v)


n = int(input().strip())

graph = [[] for _ in range(n+1)]

for _ in range(int(input().strip())):
    
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False]*(n+1)
count = 0

dfs(1)
print(count-1)