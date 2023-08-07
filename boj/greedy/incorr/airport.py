import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e4))

def find_parent(x):
    if x == parent[x]:
        
        return x
    parent[x] = find_parent(parent[x])
    return parent[x]

def union(parent,x,y):
    x = parent[x]
    y = parent[y]
    
    if x>y:
        parent[x] = y
    else:
        parent[y] = x
    

parent = [i for i in range(int(input().strip())+1)]
airplane_count = int(input().strip())

airplanes = [int(input().strip()) for _ in range(airplane_count)]

res = 0

for airplane in airplanes:
    
    find_res = find_parent(airplane)
    if find_res == 0:
        break
    union(parent,find_res,find_res-1)
    res += 1
print(res)
