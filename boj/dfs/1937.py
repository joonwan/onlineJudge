import sys
input = sys.stdin.readline

def dfs(x,y):
    dp[x][y] = 1
    now_dp = 1
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0<=nx<n and 0<=ny<n and graph[nx][ny] > graph[x][y]:
            if dp[nx][ny] == -1:
                nd = dfs(nx,ny) ## next_dp
            else:
                nd = dp[nx][ny]
            if now_dp + nd > dp[x][y]:
                dp[x][y] = now_dp + nd
 
    return dp[x][y]

n = int(input().rstrip())

graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1]*n for _ in range(n)]

dx = [1,-1,0,0]
dy = [0,0,-1,1]
max_count = 0
for i in range(n):
    for j in range(n):
        if dp[i][j] == -1:
            count = dfs(i,j)
            if count > max_count:
                max_count = count
                
print(max_count)