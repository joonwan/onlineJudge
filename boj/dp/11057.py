## 오르막수

import sys
input = sys.stdin.readline

dp = [[0]*10 for _ in range(1001)]
dp[1] = [1,1,1,1,1,1,1,1,1,1]

for i in range (2,1001):
    for j in range(len(dp[i])):
        dp[i][j] = sum(dp[i-1][j:])

n = int(input().strip())
print(sum(dp[n])%10007)