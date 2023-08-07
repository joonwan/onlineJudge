import sys
input = sys.stdin.readline

i = 1
sum = 0
s = int(input().strip())
while True:
    i += 1
 
    if sum + i >= s:
   
        break
    sum += i
    
    

print(i-1)