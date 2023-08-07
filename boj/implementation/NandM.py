import sys
input = sys.stdin.readline
from itertools import combinations

n,m = map(int, input().split())

data = [i for i in range(1,n+1)]


tes = combinations(data,m)

for l in tes:
    l = map(str,l)
    print(" ".join(l))