import sys
input = sys.stdin.readline
from collections import deque

def bfs(s):
    vtd = [False]*(n+1)
    q = deque([s])
    vtd[s] = True
    cnt = 1
    while q:
        c = q.popleft()
        for v in graph[c]:
            if not vtd[v]:
                cnt += 1
                q.append(v)
                vtd[v] = True
    return cnt
n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    graph[b].append(a)
    
max_count = 0
res = []

for i in range(1,n+1):
    count = bfs(i)
    if count > max_count:
        max_count = count
        res = [i]
    elif count == max_count:
        res.append(i)

print(*res)