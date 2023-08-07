import sys
input = sys.stdin.readline

n,m = map(int, input().split())
d = {}
for _ in range(n):
    id, pwd = input().split()
    d[id] = pwd

for _ in range(m):
    
    id = input().strip()
    ans = d[id]
    print(ans)