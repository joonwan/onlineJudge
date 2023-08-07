import sys
input = sys.stdin.readline

def find_parent(x):
    if x == parent[x]:
        return x
    
    parent[x] = find_parent(parent[x])
    return parent[x]

def union(a,b):
    a = find_parent(a)
    b = find_parent(b)
    
    if a ==b:
        return
    
    if a>b:
        parent[a] = b
    else:
        parent[b] = a
        
n = int(input().strip())
m = int(input().strip())

data = [list(map(int, input().split())) for _ in range(n)]
plan = list(map(int, input().split()))

parent = [i for i in range(n+1)]



for i in range(n):
    for j in range(n):
        
        if data[i][j] == 1:
            union(i+1, j+1)


result = set([find_parent(i) for i in plan])
if len(result) != 1:
    print("NO")
else:
    print("YES")