#다리놓기

import sys
input = sys.stdin.readline
    
def factorial(n):
    if n == 1 or n == 0:
        return 1
    
    return n*factorial(n-1)
def mCn(m,n):
    up =  factorial(m)

    down_a = factorial(m-n)
    down = factorial(n)
    return(up//(down_a*down))


def get_count(n,m):
    
    if n > m :
        return False
    
    return mCn(m,n)
        
    


t = int(input().strip())

dp = [[0]*31 for _ in range(31)]



for n in range(1,31):
    for m in range(1,31):
        
        if n == 1:
            dp[n][m] = m
        else:
            dp[n][m] = get_count(n,m)

print(dp)

for _ in range(t):
    
    n,m = map(int, input().split())
    print(dp[n][m])

