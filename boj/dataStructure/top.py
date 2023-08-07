import sys
input = sys.stdin.readline

def find(target_idx, height,idx):
    
    if target_idx == 0:
        stack.append([height,0])
        result.append(0)
        return
    
    if stack[target_idx][0] > height:
        
        stack.append([height,target_idx])
        result.append(target_idx)
        return
    else:
        find(stack[target_idx][1],height,idx) 

    
n = int(input().strip())
heights = list(map(int,input().split()))
stack = [[0,0],[heights[0],0]]
result = [0]

for i in range(1,n):
    
    height, idx = heights[i], i+1
    find(len(stack)-1,height,idx)
res = map(str,result)
print(" ".join(res))
