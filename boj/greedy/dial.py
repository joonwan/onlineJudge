import sys
input = sys.stdin.readline

data = list(map(str, input().strip()))
data.sort()

d = {}
alph = "ABCDEFGHIJKLMNO"
init = 2
for i in range(len(alph)):
    
    if i%3 == 0:
        init += 1
    d[alph[i]] = init
    
for s in "PQRS":
    d[s] = init + 1
for s in "TUV":
    d[s] = init + 2
for s in "WXYZ":
    d[s] = init + 3
    
res = 0 
for s in data:
    val = d[s]
    res += val
    
print(res)

    
    
