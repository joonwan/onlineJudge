#LCS

import sys
input = sys.stdin.readline

s1 = list(map(str, input().strip()))
s2 = list(map(str,input().strip()))

graph = [[0]*(len(s1)+1) for _ in range(len(s2)+1)]

for i in range(len(s2)):
    for j in range(len(s1)):
        if s2[i] == s1[j]:
            
            graph[i+1][j+1] = graph[i][j+1] + 1
        else:
            graph[i+1][j+1] = max(graph[i+1][j],graph[i][j+1])

print(graph[len(s2)][len(s1)])
            