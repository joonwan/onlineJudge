## 현수막

import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e6))

def dfs(x,y):

    visited[x][y] = True
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and graph[nx][ny] == 1:
            dfs(nx,ny)
    
    return True    

n,m = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]

dx = [1,-1,0,0,1,-1,-1,1]
dy = [0,0,-1,1,1,1,-1,-1]
count = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j] and graph[i][j] == 1:
            dfs(i,j)
            count += 1
    

print(count)
            