## 가장 가까운 공통조상

import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e6))

t = int(input().strip())

def dfs_2(now):
    global res
    if visited[now]:
        res = now
        return 
    
    for v in graph[now]:
        dfs_2(v)

def dfs_1(now):
    
    visited[now] = True
    for v in graph[now]:
        
        dfs_1(v)


for _ in range(t):
    
    n = int(input().strip())
    visited = [False]*(n+1)
    graph = [[] for _ in range(n+1)]
    
    for _ in range(n-1):
        a,b = map(int, input().split())
        graph[b].append(a)
    
    f_a,f_b = map(int,input().split())
    dfs_1(f_a)
    dfs_2(f_b)
    
    print(res)
    
    
    