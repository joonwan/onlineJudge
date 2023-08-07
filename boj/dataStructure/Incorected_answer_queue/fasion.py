import sys
input = sys.stdin.readline


n = int(input().strip())

for _ in range(n):
    m = int(input().strip())
    res = 1
    d = {}
    
    for _ in range(m):
        name, category = input().split()
    
        if category not in d:
            d[category] = 1
        else:
            d[category] += 1

    values = d.values()
    
    for value in values:
        
        res *= value+1
    
    print(res-1)