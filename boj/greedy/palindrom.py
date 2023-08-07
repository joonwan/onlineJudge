import sys
input = sys.stdin.readline
from collections import deque

data = list(map(str,input().strip()))
data.sort()
datas = deque()
for i in range(len(data)):
    datas.append(data[i])

void = len(data)
round = 0
flag = True
res = [None]*len(data)
ptr = 0
while datas:
    if void == 1:
        c1 = datas.popleft()
        res[ptr] = c1

        break
    while datas[0] != datas[1]:
        if round == len(datas):
            flag = False
            break
        datas.rotate(-1)
        round += 1
    
    if not flag:
        break
    round = 0
    c1 = datas.popleft()
    c2 = datas.popleft()
    res[ptr] = c1

    res[len(data)-1-ptr] = c2
    ptr += 1
    void -= 2


if flag:
    print("".join(res))
else:
    print("I'm Sorry Hansoo")