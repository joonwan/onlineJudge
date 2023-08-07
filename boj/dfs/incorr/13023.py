import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e5))


flag = False
def dfs(now,visited,dpth):
    global flag
    if dpth == 5:
        flag = True
        return 1
    visited[now] = True

   
    for v in graph[now]:
        if not visited[v]:
            if dfs(v,visited,dpth+1):
                return 1
                
            visited[v] = False

    return 0
n,m = map(int, input().split())


graph = [[] for _ in range(n)]

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n):

    visited = [False]*n
    res = dfs(i,visited,1)
    if res:
        break

if flag:
    print(1)
else:
    print(0)

