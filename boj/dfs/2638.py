import sys 
input = sys.stdin.readline
sys.setrecursionlimit(int(1e7))

def detect(x,y):
    
    air_side = 0
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0<=nx<n and 0<=ny<m:
            if graph[nx][ny] == 2:
                air_side += 1
    
    if air_side >= 2:
        return True

def dfs(x,y):
    
    visited[x][y] = True
    graph[x][y] = 2
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and graph[nx][ny] == 0:
            dfs(nx,ny)

time = 0
n,m = map(int, input().split())
dx = [1,-1,0,0]
dy = [0,0,-1,1]

graph = []
cheese = 0
for _ in range(n):
    
    data = list(map(int, input().split()))
    graph.append(data)
    for i in data:
        if i == 1:
            cheese += 1

## 구분 ## 녹을 치즈 탐지 ## 변환 ## 2->0으로 바꾸기


while cheese:
    
    ## 구분
    visited = [[False]*m for _ in range(n)]
    dfs(0,0)
    

        
    ## 녹을 치즈 선택
    melt_cheese = []
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                d = detect(i,j)
                if d:
                    melt_cheese.append((i,j))
    
    for x,y in melt_cheese:
        graph[x][y] = 2
        cheese -= 1
        
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                graph[i][j] = 0    
 
    time += 1
print(time)