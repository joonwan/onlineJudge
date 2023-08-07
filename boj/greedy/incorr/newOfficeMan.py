import sys
input = sys.stdin.readline

t = int(input().strip())
for _ in range(t):
    
    n = int(input().strip())
    data = [list(map(int,input().split())) for _ in range(n)]
    
    data.sort()
    flag = data[0][1]
    res = 1
    for i in range(1,len(data)):
        if data[i][1] < flag:
            flag = data[i][1]
            res += 1
    print(res)
    