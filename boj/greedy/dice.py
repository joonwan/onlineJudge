import sys
input = sys.stdin.readline

n = int(input().strip())
a = list(map(int, input().split()))


min_list = []

for i in range(3):
    
    min_list.append(min(a[i],a[5-i]))
min_list.sort()

d = min_list[0]
b = min_list[0] + min_list[1]
c= sum(min_list)


## a -> three select


    

if n == 1:
    res = sum(a) - a[a.index(max(a))]
else:
    
    one = (4*(n-1)*(n-2) + (n-2)**2)*d
    two = (4*(n-1) + 4*(n-2))*(b)
    three = 4*c
    
    res = one+two+three

print(res)

