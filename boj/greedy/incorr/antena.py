import sys
input = sys.stdin.readline

n = int(input().strip())
data = list(map(int,input().split()))
data.sort()

print(data[(len(data)-1)//2])