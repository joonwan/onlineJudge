import sys
input = sys.stdin.readline
from collections import deque

def get_time(direction_change):
    time = 0
    direction =deque([(0,1), (-1,0), (0,-1), (1,0)])
    defalt_direction = direction[0]
    length = 1
    now = deque()
    body = deque()
    body.append([0,0])
    now.append([0,0])
    while True:
        x,y = now.popleft()
        
        for t,nd in direction_change:
            if time == t:
                if nd == "L":
                    direction.rotate(-1)
                else:
                    direction.rotate(1)
        nx, ny = x + direction[0][0] , y + direction[0][1]
        
        if 0<= nx < n and 0<=ny < n and graph[nx][ny]:
           
            if graph[nx][ny] == "apple":
                
                graph[nx][ny] = False
                now.append([nx,ny]) 
                body.appendleft([nx,ny])
                length += 1
                time += 1
              
            else:
                a,b = body.pop()
                graph[a][b] = True
                body.appendleft([nx,ny])
                graph[nx][ny] = False
                now.append([nx,ny])
                time += 1
               
            
        else:
            time += 1
            break
      
    return time
# nxn
n = int(input().strip())

graph = [[True]*n for _ in range(n)]
graph[0][0] = False
# apple 
apple_num = int(input().strip())
apple_location = []
for _ in range(apple_num):
    x,y = map(int, input().split())
    graph[x-1][y-1] = "apple"

## direction change time and direction
direction_change = []

dc_num = int(input().strip())
for _ in range(dc_num):
    time, direction = map(str, input().split())
    direction_change.append((int(time), direction))



time = get_time(direction_change)
print(time)


