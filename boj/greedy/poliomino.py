import sys
input = sys.stdin.readline
from collections import deque
data = input().strip()
l_data = list(map(str, data))
s_data = data.split(".")
r_s_data = []
for s in s_data:
    if 'X'  in s:
        r_s_data.append(s)

res = deque()
flag = True
for data in r_s_data:
    
    if len(data)>=4:
        
        r = len(data)%4
        
        if r%2 != 0:
            flag = False
            break
        else:
            four_num = len(data)//4
            two_num = (r%4)//2
            
            for _ in range(4*four_num):
                res.append("A")
            
            for _ in range(2*two_num):
                res.append("B")
    
    elif len(data) < 4:
        
        if len(data)%2 == 0:
            
            for _ in range(2*len(data)//2):
                
                res.append("B")
        else:
            flag = False
            break



if flag:
    for i in range(len(l_data)):
    
        if l_data[i] == "X":
        
            d = res.popleft()
            l_data[i] = d
    
    print("".join(l_data))

else:
    print(-1)    