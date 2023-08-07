import sys
input = sys.stdin.readline

n = int(input().strip())
crane = list(map(int, input().split()))
crane.sort(reverse=True)
m = int(input().strip())
boxes = list(map(int, input().split()))
boxes.sort(reverse=True)
cranes =  []
max_count = 0 
flag = False
for c in crane:
    cranes.append([c,0])

for box in boxes:
    
    can_input = []
   
    for c in cranes:
        
        if box <= c[0]:
            can_input.append(c)
    if can_input == []:
        flag = True
        break
    
    can_input = sorted(can_input, key=lambda x:x[1])
    target = can_input[0]

    for i in range(len(cranes)):
        if cranes[i] == target:
 
            cranes[i][1] += 1
   
            if max_count < cranes[i][1]:
                max_count = cranes[i][1]
            break

if flag:
    print(-1)
else:
    print(max_count)