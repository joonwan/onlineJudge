n = int(input().strip())
li =[]
for i in range(n):  #data = [tuple(map(int, input().split())) for _ in range(n)]
    a,b = map(int,input().split())
    li.append((a,b))
ans=[]

for j in li:
    t=1
    for k in li:
        if j[0] < k[0] and j[1] < k[1]:
            t += 1
    ans.append(t)


ans = map(str,ans)
ans =" ".join(ans)
print(ans)