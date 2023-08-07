import sys
input = sys.stdin.readline
# import copy

def find(start):
    
    global count
    x,y = start

    graph[x][y] = 'x'

    if y == m-1:
        count += 1
        return True
    
    dx = [-1,0,1]
    
    for i in range(3):
        nx = x + dx[i]
        ny = y + 1
        
        if 0<=nx<n and 0<=ny < m and graph[nx][ny] != 'x':
            if find((nx,ny)):
             return True
                
        
    return False
        
n,m = map(int,input().split())

graph = [list(map(str,input().strip())) for _ in range(n)]
count = 0


for start in [(i,0) for i in range(n)]:
 
    # tmp = copy.deepcopy(graph)
    tmp = graph
    t = find(start)
 
    if not t:
        graph = tmp


print(count)