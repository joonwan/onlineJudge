import sys
input = sys.stdin.readline

num = input().strip()
n = len(num) 

res = (int(num) - 10**(n-1) + 1)*n
n -= 1

while n > 0:
  
    res += (10**n-1 - 10**(n-1) + 1)*n
    n -= 1
    
    
print(res)