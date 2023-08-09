# 침투
import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e6))

def dfs(x,y):
    visited[x][y] = True
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and graph[nx][ny] == 0:
            dfs(nx,ny)


n,m = map(int,input().split())
graph = [list(map(int,input().strip())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]

start = [(0,i) for i in range(m)]

dx = [1,-1,0,0]
dy = [0,0,-1,1]

for s in start:
    
    x,y = s
    if not visited[x][y] and graph[x][y] == 0:
        dfs(x,y)

if True in visited[n-1]:
    print("YES")
else:
    print("NO")
        
