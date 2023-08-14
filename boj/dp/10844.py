#쉬운 계단수

import sys
input = sys.stdin.readline

dp = [[0]*10 for _ in range(101)]
dp[1] = [0,1,1,1,1,1,1,1,1,1]
dp[2] = [1,1,2,2,2,2,2,2,2,1]
produce = [1,2,2,2,2,2,2,2,2,1]



for i in range(2,100):
    
    for j in range(0,10):
        if j == 0:
            dp[i+1][1] += dp[i][0]
        elif j == 9:
            dp[i+1][8] += dp[i][9]
        else:
            dp[i+1][j-1] += dp[i][j]
            dp[i+1][j+1] += dp[i][j]
                
n = int(input().strip())
print(sum(dp[n])% 1000000000)