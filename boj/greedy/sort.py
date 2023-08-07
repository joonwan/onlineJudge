import sys
input = sys.stdin.readline

n = int(input().strip())
think = [0]
for _ in range(n):
    think.append(int(input().strip()))
think.sort()
res = 0
for i in range(1,n+1):
    res += abs(i-think[i])
print(res)
