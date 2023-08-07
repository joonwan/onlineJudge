import sys
from collections import deque
input = sys.stdin.readline

s = input().strip()
t = deque(map(str, input().strip()))
rev = False ## reverse

for _ in range(len(t)-len(s)):
    
    if not rev:
        char = t.pop()
    else:
        char = t.popleft()
        
    if char == "B":
        if rev:
            rev = False
        else:
            rev = True

t = list(t)
if rev:
    t.reverse()

if s == "".join(t):
    print(1)
else:
    print(0)
