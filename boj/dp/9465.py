## 스티커

import sys
input = sys.stdin.readline

t = int(input().strip())

for _ in range(t):
    
    n = int(input().strip())
    count = 0
    graph = [list(map(int, input().split())) for _ in range(2)]
    
    if n == 1:
        print(max(graph[0][n-1], graph[1][n-1]))
        count += 1
        continue
    
    if n == 2:
        print(max(graph[1][0] + graph[0][1], graph[0][0]+ graph[1][1]))
        continue
    dp = [[0]*n for _ in range(2)]
    
    dp[0][0] = graph[0][0]
    dp[1][0] = graph[1][0]
    
    dp[0][1] = graph[0][1] + dp[1][0]
    dp[1][1] = graph[1][1] + dp[0][0]
    
    for j in range(2,n):
        for i in range(2):
            if i == 0:
                dp[i][j] = graph[i][j] +  max(dp[1][j-1], max(dp[0][j-2],dp[1][j-2]))
            else:
                 dp[i][j] = graph[i][j] +  max(dp[0][j-1], max(dp[0][j-2],dp[1][j-2]))
    
    print(max(dp[0][n-1],dp[1][n-1]))