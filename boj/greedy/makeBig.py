import sys
input = sys.stdin.readline

stack = []


n,m = map(int, input().split())
flag = True
datas = list(map(int, input().strip()))

stack.append(datas[0])

for i in range(1,len(datas)):
    
    if m > 0:
        if stack:
            while m and  stack and (stack[-1] < datas[i]):
                stack.pop()
                m -= 1
            
            stack.append(datas[i])
    
    else:
        stack.append(datas[i])

if len(stack) != (n-m):
    
    for i in range(m):
        stack.pop()
stack = map(str, stack)
print("".join(stack))