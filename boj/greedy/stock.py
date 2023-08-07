import sys
input = sys.stdin.readline

t = int(input().strip())
for _ in range(t):
    l = int(input().strip())
    data = list(map(int,input().split()))
    data.reverse()
    max_val = 0
    m_val_list = []
    for d in data:
        if max_val < d:
            max_val = d
        m_val_list.append(max_val)
       
            
    res = 0
    
    for i in range(l):
        res += m_val_list[i] - data[i]
    print(res)