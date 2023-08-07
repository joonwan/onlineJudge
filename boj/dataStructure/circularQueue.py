from collections import deque
import sys

input = sys.stdin.readline

n,m = map(int, input().split())
targets = list(map(int, input().split()))
q = deque([i for i in range(1,n+1)])
count = 0
for target in targets:
    
    while True:
        
        if q[0] == target:
            q.popleft()
   
            break
        
        else:
            if q.index(target) < len(q)/2:
                
                while q[0] != target:
                    q.rotate(-1)
                    count += 1
             
            else:
                while q[0] != target:
                    q.rotate(1)
                    count += 1
                    
                
print(count)
                