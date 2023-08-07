## 양
## . 빈공간 # 울타리, o 양, v 늑대
import sys
sys.setrecursionlimit(int(1e6))

def dfs(x,y):
    global o
    global v
    
    visited[x][y] = True
    
    if graph[x][y] == "v":
        v += 1
    elif graph[x][y] == "o":
        o += 1
    
    for i in range(4):
        
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0<=nx<n and 0<=ny<m and graph[nx][ny] != "#" and not visited[nx][ny]:
            
            dfs(nx,ny)
    
input = sys.stdin.readline

total_o = 0 ## 총 양
total_v = 0 ## 총 늑대

n,m = map(int,input().split())
graph = [list(map(str,input().strip())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]

dx = [1,-1,0,0]
dy = [0,0,-1,1]
for i in range(n):
    for j in range(m):
        if graph[i][j] != "#" and not visited[i][j]:
            o = 0
            v = 0
           
            dfs(i,j)
           
            if o > v:
                total_o += o
            elif o <= v:
                total_v += v
            
print(total_o, total_v)