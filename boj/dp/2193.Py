## 이친수

dp = [[0,0] for _ in range(91)]
dp[1] = [1,0]

for i in range(1,90):
    
    one = dp[i][0]
    zero = dp[i][1]
    
    dp[i+1][1] += one
    dp[i+1][0] += zero
    dp[i+1][1] += zero

print(sum(dp[int(input().strip())]))