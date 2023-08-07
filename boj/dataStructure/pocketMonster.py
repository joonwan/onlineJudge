import sys
input = sys.stdin.readline
n,m = map(int, input().split())
dname = {}
dnum = {}
for i in range(1,n+1):
    name = input().strip()
    dname[name] = i
    dname[str(i)] = name
for _ in range(m):
    try:
        answer = dname[input().strip()]
        print(answer)
    except:
        answer = dnum[input().strip()]
        print(answer)
