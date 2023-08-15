# 카드 구매하기

n = int(input().strip())
data = list(map(int, input().split()))
val = [0]

for d in data:
    val.append(d)
    
dp = [0 for _ in range(n+1)]
dp[1] = val[1]

    
for i in range(2,n+1):
    
    temp = [val[i]]
    for j in range(i-1,i//2-1,-1):
        temp.append(dp[j] + dp[i-j])

    dp[i] = max(temp)

print(dp)



    
