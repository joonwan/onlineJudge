import sys
input = sys.stdin.readline

n = int(input().strip())
datas = [int(input().strip()) for _ in range(n)]

ptr = 0
stack = []
res = ""
flag = True
for data in datas:
    
    if ptr < data:
        for i in range(ptr+1,data+1):
            stack.append(i)
            res += "+"
        stack.pop()
        res+="-"
        ptr = data
    elif ptr > data:
        if stack[-1] != data:
            flag = False
            break
        elif stack[-1] == data:
            res += "-"
            stack.pop()

if flag:
    for s in res:
        print(s)
else:
    print("NO")