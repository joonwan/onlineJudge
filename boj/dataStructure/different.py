import sys
input = sys.stdin.readline

string = input().strip()
d = {}
for i in range(len(string)+1):
    
    for j in range(i+1,len(string)+1):
    
        if string[i:j] not in d:
            d[string[i:j]] = 1

print(len(d))
    

    