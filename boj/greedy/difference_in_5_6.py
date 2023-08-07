import sys
input = sys.stdin.readline

nums = input().split()

### min
res = []
for num in nums:
    
    num_arr = list(map(str, num))
    
    for i in range(len(num_arr)):
        if num_arr[i] == "6":
            num_arr[i] = "5"
            
    res.append("".join(num_arr))

min = int(res[0]) + int(res[1])


res = []
for num in nums:
    
    num_arr = list(map(str, num))
    
    for i in range(len(num_arr)):
        if num_arr[i] == "5":
            num_arr[i] = "6"
            
    res.append("".join(num_arr))

max = int(res[0]) + int(res[1])

print(min,max)
