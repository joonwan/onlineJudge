import sys
input = sys.stdin.readline

n,m = map(int, input().split())
graph = [list(map(int,input().strip())) for _ in range(2*n)]
count = 0

original = []
target = []




for i in range(len(graph)):
    
    if i < n:
        original.append(graph[i])
    else:
        target.append(graph[i])
        
if n < 3 or m <3:
    if original == target:
        print(0)
    else:
        print(-1)
    exit()
for i in range(n-2):
  
    
    for j in range(m-2):
   
       
       if original[i][j] == target[i][j]:
           continue
       
       else:
         
            count += 1
            for a in range(i,3+i):
               for b in range(j, j+3):
                    if original[a][b] == 1:
                        original[a][b] = 0
                    else:
                        original[a][b] = 1
 

if original == target:
    print(count)
else:
    print(-1)