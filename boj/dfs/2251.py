import sys
input = sys.stdin.readline
import copy
def dfs(start,visited,init_val):

    if init_val[1] == 0:
        if init_val[3] not in res:
            res.add(init_val[3])
  
   
    visited[start] = True
    
    for v in graph[start]:
        
        if v == 3 and visited[v]:
            if (init_val[1] + init_val[3]) not in res:
                res.add(init_val[1] + init_val[3])
                
                
        
        if not visited[v]:
            
            tmp = copy.deepcopy(init_val)
            
            if val[v] >= val[start]:
               
                tmp[v] = val[start]
                tmp[start] = 0
            else:
                
                tmp[start] -= val[v]
                tmp[v] = val[v]
            
            dfs(v,visited,tmp)
            
            
            visited[v] = False
  
               
    
    
    

node = [1,2,3]
val = [0]

for v in list(map(int, input().split())):
    val.append(v)
init_val = [0,0,0,val[-1]]
visited = [False]*4
res= set()

graph = [[] for _ in range(4)]
for i in range(1,4):
    for j in range(1,4):
        if i!=j:
            graph[i].append(j)

dfs(3,visited,init_val)


a = [0,0,val[3]-val[1],val[1]]
b = [0,0,val[2],val[3]-val[2]]

for t in [a,b]:
    
    for i in range(1,3):
        if t[0] + t[i] not in res:
            res.add(t[0]+t[i])

res = list(res)
res.sort()

res = map(str,res)
print(" ".join(res))