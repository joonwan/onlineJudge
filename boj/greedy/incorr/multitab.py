import sys
input = sys.stdin.readline
import heapq
from collections import deque

n,m = map(int, input().split())
data = list(map(int, input().split()))
heap = []
in_data = []
total_data = deque()
for i in range(len(data)):
    
    if data.count(data[i]) == 1:
        total_data.append((1,data[i]))
    else:
        if data[i] not in in_data:
            start_idx = data.index(data[i])
            max_idx = 0
            for j in range(i,len(data)):
                if data[i] == data[j]:
                    if i < j:
                        max_idx = j
        
            in_data.append(data[i])
            total_data.append((max_idx,data[i]))
print(total_data)
for _ in range(n):
    d= total_data.popleft()
    heapq.heappush(heap,d)
res = 0
for _ in range(len(total_data)):
    
    heapq.heappop(heap)
    d = total_data.popleft()
    heapq.heappush(heap,d)
    res += 1

print(res)