import sys
input = sys.stdin.readline

matrix1 = []
matrix2 = []


for i in range(2):
    n,m = map(int, input().split())
    
    for j in range(n):
        data = list(map(int, input().split()))
        if i == 0:
            matrix1.append(data)
        else:
            matrix2.append(data)

for d1,d2 in matrix1:
    
    for i in range(len(matrix2[0])):
        k1,k2  = matrix2[]