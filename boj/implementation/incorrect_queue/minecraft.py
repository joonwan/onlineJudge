import sys
input = sys.stdin.readline
res_time = 0
d = {}
m_height = 0
n,m,b = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        
        height = graph[i][j]
        if m_height < height:
            m_height = height
            
        if height in d:
            d[height] += 1
        else:
            d[height] = 1

while len(d) != 1:
    
    max_count = d[m_height]
    
    pop_time = max_count*2
    put_time = (n*m-max_count)
    
    if (pop_time < put_time) or (b < n*m-max_count):
        
        res_time += pop_time
        nxt_m_height = m_height - 1
        b += max_count
        if nxt_m_height in d:
            d[nxt_m_height] += d[m_height]
        else:
            d[nxt_m_height] = d[m_height]

        del d[m_height]
 