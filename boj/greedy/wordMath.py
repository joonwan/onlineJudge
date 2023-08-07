import sys
input = sys.stdin.readline

n = int(input().strip())
datas = []
d_pri = {}
d_ten = {}
for _ in range(n):
    data = input().strip()
    datas.append(data)
    
    for i in range(len(data)):
        s = data[i]
        if s not in d_pri:
            d_pri[s] = 10**(len(data)-i-1)
        else:
            d_pri[s] += 10**(len(data)-i-1)
        
d_l = []
d_in = []
for data in datas:
    for s in data:
        if s not in d_in:
            d_l.append((d_pri[s],s))
            d_in.append(s)
d_l.sort(reverse=True)
head = 9
for val ,alph in d_l:
    d_pri[alph] = head
    head -= 1

res = 0
for data in datas:
    for i in range(len(data)):
        res += d_pri[data[i]]*10**(len(data)-1-i)
        
print(res)