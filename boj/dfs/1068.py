import sys
input = sys.stdin.readline


def dfs(start):
    global count 
    if start == delete_node_num:
        return
    visited[start] = True
    if graph[start] == []:
        count += 1
        return
    for v in graph[start]:
        if not visited[v]:
            dfs(v)
    
    return
        
    
count = 0
n = int(input().rstrip()) ## node 개수
parents = list(map(int, input().split()))
delete_node_num = int(input().rstrip())

graph = [[] for _ in range(n)]
start = 0
for i in range(len(parents)):
    if parents[i] == -1:
        start = i
        continue
    
    if i == delete_node_num:
        continue
    
    graph[parents[i]].append(i)
graph[delete_node_num] = []
visited = [False]*n

dfs(start)
print(count)