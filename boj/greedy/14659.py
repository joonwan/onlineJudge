## 힌저서열 정리하고옴 ㅋㅋ

import sys
input = sys.stdin.readline

n = int(input().strip())
data = list(map(int,input().split()))

count = [0]*(n)
stack = [data[0]]
high_idx = 0
for i in range(1,n):
    
    now = data[i]

    if stack[-1] > now:
        count[high_idx] += 1
    
        
    elif stack[-1] < now:
        high_idx = i
        stack.append(data[i])

print(max(count))