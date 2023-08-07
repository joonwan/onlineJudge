import sys
input = sys.stdin.readline
import heapq

n,m = map(int, input().split())

heap = []
res = []
for _ in range(m):
    
    num1, num2 = map(int, input().split())
    
    heapq.heappush(heap, (num1, num2))

for _ in range(len(heap)):
    num1, num2 = heapq.heappop(heap)
    res.append(num1)
    res.append(num2)
    
res = map(str, res)
print(" ".join(res))