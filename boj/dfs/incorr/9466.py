import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e7))

t = int(input().rstrip())

def dfs(now):
    global group
    visited[now] = True
    cycle.append(now)
    nxt_node = graph[now][0]
    
    if visited[nxt_node]:
        if nxt_node in cycle:
            group += cycle[cycle.index(nxt_node) :]
            return
    else:
        dfs(nxt_node)
    
    
    
for _ in range(t):
    
    n = int(input().rstrip())
    data = list(map(int, input().split()))
    graph = [[] for _ in range(n+1)]
    
    for i in range(n):
        graph[i+1].append(data[i])
    
    visited = [False]*(n+1)
    group = []
    for i in range(1,n+1):

        if not visited[i]:
            cycle = []
            dfs(i)
    
    print(n-len(group))