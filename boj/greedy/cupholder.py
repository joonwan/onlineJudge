import sys
input = sys.stdin.readline

n = int(input().strip())
data = list(map(str,input().strip()))

l_count = 0
res = 1
for d in data:
    
    if d == "S":
        res += 1
    else:
        l_count += 1
        
        if l_count == 2:
            l_count = 0
            res += 1
        
  
if res > n:
    res = n
print(res)
            
        
    