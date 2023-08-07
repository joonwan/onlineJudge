import sys
input = sys.stdin.readline

n = int(input().strip())

if n == 1:
    input()
    print(0)
    exit()
    
data = [int(input().strip()) for _ in range(n)]
flag = data[0]
first = data[0]
data = data[1:]
data.sort(reverse=True)

while data[0] >= flag:
    flag += 1

    data[0] -= 1
    data.sort(reverse=True)


res = flag-first
print(res)


