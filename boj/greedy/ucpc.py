import sys
input = sys.stdin.readline

stack =  []
ans = ["U","C","P","C"]
ans.reverse()

for s in ans:
    stack.append(ord(s))



datas = input().split()
flag = True
res_flag = True
for data in datas:
    if not flag:
        break
    for s in data:
        if not flag:
            break
        if stack and stack[-1] == ord(s) :
            stack.pop()
            if not stack:
                break

if stack:
    print("I hate UCPC")  
else:
    print("I love UCPC")
