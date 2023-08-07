import sys
input = sys.stdin.readline

n = int(input().strip())

datas = [tuple(map(int, input().split())) for _ in range(n)]

count = [1]*n

for i in range(len(datas)):
    w,h = datas[i]
    
    for j in range(len(datas)):
        if i == j:
            continue
        n_w, n_h = datas[j]
        if w < n_w and  h <n_h:
            count[i] += 1
res = map(str,count)
res = " ".join(res)
print(res)