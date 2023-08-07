from collections import deque

def bfs(start):
    
    q = deque()
    q.append(start)
    visited[start] = True
    while q:
        now = q.popleft()
        
        print(now, end=" ")
        for v in graph[now]:
            if not visited[v]:
                q.append(v)
                visited[v] = True


graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False]*9

bfs(1)
