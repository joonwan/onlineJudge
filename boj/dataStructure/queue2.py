import sys
input = sys.stdin.readline
from collections import deque

method = ["push","pop","size","empty","front","back"]

n = int(input().strip())
q = deque()

for _ in range(n):
    
    datas = input().split()
    if len(datas) == 2:
        m = datas[0]
        data = datas[1]
    else:
        m = datas[0]
    
    if m == method[0]:
        q.append(data)
    
    elif m == method[1]:
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())
    elif m == method[2]:
        print(len(q))
    elif m == method[3]:
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif m == method[4]:
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
    
    elif m == method[5]:
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])
        