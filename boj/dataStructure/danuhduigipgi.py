import sys
input = sys.stdin.readline
stack = []

string = input().strip()
flag = False
res = ""
for s in string:
    if s == "<":
        flag = True
        if stack:
  
            for _ in range(len(stack)):
                data = stack.pop()
                res += data
     
        stack.append("<")
    elif s == " ":
        if not flag:
            for _ in range(len(stack)):
                data = stack.pop()
                res += data
            res += " "
        else:
            stack.append(" ")
    elif s == ">":
        flag = False
        stack.append(">")
        res += "".join(stack)
        stack = []
    else:
        stack.append(s)

if stack:
    stack.reverse()
    res += "".join(stack)
print(res)
