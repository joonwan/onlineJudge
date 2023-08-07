def dfs(now, visited,graph):
    
    visited[now] = True
    
    for v in graph[now]:
        if not visited[v]:
            dfs(v,visited,graph)
    
    return True

def solution(n, computers):
    answer = 0
    

    graph = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j] == 1:
                graph[i].append(j)
                
    visited = [False]*n
    
    
    for i in range(n):
        if not visited[i]:
            res=dfs(i,visited,graph)
            if res:
                answer += 1
            
    
    return answer