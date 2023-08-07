import sys
input = sys.stdin.readline
import heapq
m_val =  32001
n,m = map(int, input().split())
heap = []
already = set()
res = []
for _ in range(m):
    a,b = map(int,input().split())
    if a < b:
        continue
    else:
        heap.append((a,b))
        already.add(a)
        already.add(b)

# for i in range(1,n+1):
#     if i in already:
#         continue
#     heap.append((m_val,i))
heap = sorted(heap, key=lambda x:x[1])

for x,y in heap:
    if x == m_val:
        res.append(y)
    else:
        res.append(x)
        res.append(y)
res = map(str, res)
print(" ".join(res))
    
    