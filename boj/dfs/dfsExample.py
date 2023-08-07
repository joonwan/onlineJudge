def dfs(start):
    
    visited[start] = True
    
    print(start, end = " ")
    
    vector = graph[start]
    
    for v in vector:
        if not visited[v]:
            dfs(v)
    

visited = [False]*9


graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

dfs(1)