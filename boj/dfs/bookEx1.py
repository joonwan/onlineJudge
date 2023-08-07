## 음료수 얼려먹기
from collections import deque
# 00110
# 00011
# 11111
# 00000

def bfs(a,b):
    
    q = deque()
    q.append((a,b))
    graph[a][b] = 1
    
    while q:
        x,y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<n and 0<=ny<m and graph[nx][ny] != 1:
                q.append((nx,ny))
                graph[nx][ny] = 1
    
    return True

n,m = map(int, input().split())

graph = [list(map(int, input().strip())) for _ in range(n)]

dx = [1,-1,0,0]
dy = [0,0,-1,1]

count = 0

for i in range(n):
    for j in range(m):
        
        if graph[i][j] == 0:
            if bfs(i,j):
                count += 1

print(count)