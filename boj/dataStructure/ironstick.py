import sys
input = sys.stdin.readline

data = input().strip()
stack = []
res = 0
for s in data:
    if s == "(":
        stack.append(["(",0])
    
    if s == ")":
        out = stack.pop()
        if out[1] == 0:
            
            for k in stack:
                k[1] += 1
        else:
            res += out[1] +1
            
print(res)