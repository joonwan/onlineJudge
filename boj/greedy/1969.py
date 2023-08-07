import sys
input = sys.stdin.readline
from collections import Counter

n,m = map(int, input().split())

data = [input().strip() for _ in range(n)]
res = ""
hd = 0
for j in range(m):
    nucleotide = []
    for i in range(n):
        nucleotide.append(data[i][j])
    c = Counter(nucleotide).most_common()
    c = sorted(c, key=lambda x:(-x[1],x[0]))
    res += c[0][0]
print(res)

for d in data:
    
    for i in range(len(d)):
        if res[i] != d[i]:
            hd += 1

print(hd)