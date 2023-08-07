import sys
from collections import deque
input = sys.stdin.readline

n = int(input().strip())

for _ in range(n):
    flag = True
    r = 0
    method = input().strip()
    length = int(input().strip())
    data = deque(input().strip()[1:-1].split(","))
    
    if length == 0:
        data = deque()
    
    for m in method:
        if m == "R":
            r += 1

        elif m == "D":
            if len(data) == 0:
                flag = False
                
                break
            if r%2 == 0:
                data.popleft()
            else:
                data.pop()
    
    if flag:
        data = list(data)
        if r%2 != 0:
            data.reverse()
        print("[" + ",".join(data) + "]")
    else:
        print("error")