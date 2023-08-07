import sys
input = sys.stdin.readline

n,m = map(int, input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

k = int(input().strip())

for _ in range(k):
    res = 0
    i,j,x,y = map(int, input().split())
    
    for a in range(i-1,x):
        for b in range(j-1, y):
            
            res += graph[a][b]
    
    print(res)