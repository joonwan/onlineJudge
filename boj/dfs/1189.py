## 컴백홈

import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e6))

def dfs(x,y,distance):
    global count
    if distance == k  and x == n-1 and y == 0:
        count += 1
    visited[x][y] = True
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and graph[nx][ny] != "T":
            dfs(nx,ny,distance+1)
            visited[nx][ny] = False
            
    
    

n,m,k = map(int,input().split())

graph = [list(map(str,input().strip())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]

dx = [1,-1,0,0]
dy = [0,0,-1,1]
count = 0
dfs(0,m-1,1)
print(count)
