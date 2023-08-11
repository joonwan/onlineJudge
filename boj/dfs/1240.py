## 노드 사이의 거리

import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e6))

def dfs(now,target):

    global val
    visited[now] = True
    if now == target:
        return True

    for nxt_node,distance in graph[now]:
        if not visited[nxt_node]:
            val += distance
            res = dfs(nxt_node,target)
            if res:
                return True
            else:
                val -= distance
    return False

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    n1,n2,d = map(int,input().split())
    graph[n1].append((n2,d))
    graph[n2].append((n1,d))

for _ in range(m):
    visited = [False]*(n+1)
    start,target = map(int,input().split())
    val = 0
    res = dfs(start,target)

    print(val)
    