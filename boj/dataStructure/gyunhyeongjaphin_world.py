import sys
input = sys.stdin.readline

while(1):
    stack = []
    VPS = True
    string =input()
    if string[0] == ".":
        break
    
    for s in string:
        
        if len(stack) == 0 and (s == ")" or s =="]"):
            VPS = False
            break
        
        elif s == "(" or s == "[":
            stack.append(s)
        elif s == ")" :
            if stack[-1] == "(":
                stack.pop()
            else:
                VPS = False
                break
        elif s == "]":
            if stack[-1] == "[":
                stack.pop()
            elif stack[-1] != "[":
                VPS = False
                break
    
   
    if len(stack) != 0:
        VPS = False
    if VPS:
        print("yes")
    else:
        print("no")
    
    
    
    
