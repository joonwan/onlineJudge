import sys
input = sys.stdin.readline
import heapq

n = int(input().strip())
res = 0
homeWork = [tuple(map(int, input().split())) for _ in range(n)]
homeWork = sorted(homeWork, key = lambda x:(x[0],x[1]))
heap = []
day = 0

for d_day, value in homeWork:
    
    if day < d_day:
        heapq.heappush(heap,(value,d_day))
        day += 1
    else:
        min_val,min_d_day = heapq.heappop(heap)
        if min_val < value:
            heapq.heappush(heap,(value,d_day))
        else:
            heapq.heappush(heap,(min_val,min_d_day))
   
for i in range(len(heap)):
    res += heap[i][0]

print(res)

