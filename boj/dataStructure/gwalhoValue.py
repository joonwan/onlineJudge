import sys
input =sys.stdin.readline

res = 0
flag = True

stack = []

string = input().strip()

for s in string:
    
    if not stack:
        if s == ")" or s == "]":
            flag = False
            break
    
    if s == "(":
        stack.append(["(",0])
    elif s == "[":
        stack.append(["[",0])
        
    elif s == "]":
        if stack[-1][0] != "[":
            flag = False
            break
        else:
            data, val = stack.pop()
            if not stack:
                if val == 0:
                    res += 3
                else:
                    res += 3*val
            else:
                if val == 0:
                    stack[-1][1] += 3
                else:
                    stack[-1][1] += 3*val
    elif s == ")":
        if stack[-1][0] != "(":
            flag = False
            break
        else:
            data, val = stack.pop()
            
            if not stack:
                if val == 0:
                    res += 2
                else:
                    
                    res += 2*val
            else:
                if val == 0:
                    stack[-1][1] += 2
                else:
                    stack[-1][1] += 2*val

if flag:
    print(res)
else:
    print(0)