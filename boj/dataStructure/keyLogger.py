from collections import deque
import sys
input = sys.stdin.readline

n = int(input().strip())

for _ in range(n):
    
    data = input().strip()
    stack = deque()
    tmp = deque()
    for s in data:
        
        if s == "-":
            if stack:
                stack.pop()
        
        elif s == ">":
            
            if tmp:
                
                d = tmp.pop()
                stack.append(d)
        elif s == "<":
            
            if stack:
                d = stack.pop()
                tmp.append(d)
        else:
            stack.append(s)
    
    if tmp:
        for _ in range(len(tmp)):
            d = tmp.pop()
            stack.append(d)
    print("".join(stack))