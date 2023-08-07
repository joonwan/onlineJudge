import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e6))


def dfs(now,num):
    
    group[now] = num
    
    for nxt in graph[now]:
        if group[nxt] == 0:
            res = dfs(nxt,-num)
            if not res:
                return False
        else:
            if group[now] == group[nxt]:
                return False
    
    return True
     

t = int(input().strip())

for _ in range(t):
    v,e = map(int,input().split())
    graph = [[] for _ in range(v+1)]
    group = [0 for _ in range(v+1)]
    
    for _ in range(e):
        a,b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    for i in range(1,v+1):
        if group[i] == 0:
            res = dfs(i,1)

            if not res:
                break
    
    if res:
        print("YES")
    else:
        print("NO")
        