import sys
from collections import deque
input = sys.stdin.readline

methods = ["L", "D", "B", "P"]

string = deque(list(map(str,input().strip())))

n = int(input().strip())
tmp = deque()
for _ in range(n):
    data = input().split()
    if len(data) == 2:
        method = data[0]
        val = data[1]
    else:
        method = data[0]
      
    if method == methods[0]:
        
        if  string:
            
            t = string.pop()
            tmp.append(t)
            
    elif method == methods[1]:
        if  tmp:
            t = tmp.pop()
            string.append(t)
    elif method == methods[2]:
        if  string:
            string.pop()
    
    elif method == methods[3]:
        string.append(val)

if tmp:
    while tmp:
        t = tmp.pop()
        string.append(t)

print("".join(string))