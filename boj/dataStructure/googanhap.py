import sys
input = sys.stdin.readline

n,m,k = map(int, input().split())

## set size of segment tree
size = 1
up = 1 ## 승
while True:
    
    size = size*(2**up)
    up += 1
    if size >= n:
        break
      
size = size*2

## init segment tree

tree = [0]*size
reef_idx = 2**up

for i in range(n):
    num = int(input().strip())
    tree[reef_idx] = num
    
    reef_idx += 1


