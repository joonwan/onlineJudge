import sys
input =sys.stdin.readline

stack = []

string = list(map(str, input().strip()))
boom = list(map(str, input().strip()))
l = len(boom)

for s in string:
    stack.append(s)
    
    if len(stack) >= l:
        if stack[-l:] == boom:
            for _ in range(l):
                stack.pop()
    
    
if stack:
    print("".join(stack))
else:
    print("FRULA")

