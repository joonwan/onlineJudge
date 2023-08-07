import sys
input = sys.stdin.readline

n = int(input().strip())
house = int(input().strip())

if n <= house:
    print(0)
    exit()
sensors = list(map(int,input().split()))
sensors.sort()
distance = []
for i in range(1,len(sensors)):
    d = sensors[i] - sensors[i-1]
    distance.append(d)
set_num = 1

distance.sort()



while set_num != house:
    distance.pop()
    set_num += 1
   
    
print(sum(distance))
