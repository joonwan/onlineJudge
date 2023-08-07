import sys
input = sys.stdin.readline

n = int(input().strip())
s = set()

for _ in range(n):
    
    methods = input().split()
    
    if len(methods) > 1:
        method = methods[0]
        val = int(methods[1])
    else:
        method = methods[0]
    
    if method == "add":
        if val not in s:
            s.add(val)
            
    elif method == "remove":
        s.discard(val)
    
    elif method == "check":
        
        if val in s:
            print(1)
        else:
            print(0)
    
    elif method == "toggle":
        
        if val in s:
            s.discard(val)
        else:
            s.add(val)
    
    elif method == "all":
        s = set(list(i for i in range(1,21)))
    
    elif method == "empty":
        s = set()
   
