import sys
input = sys.stdin.readline

n = int(input().strip())
nums = list(map(int, input().split()))
res = [-1]*n
stack = []
stack.append((0,nums[0]))

for i in range(1, n):
   
    while stack and stack[-1][1] < nums[i]:
       
        idx, num = stack.pop()
        res[idx] = nums[i]

    stack.append((i,nums[i]))
 
res = map(str, res)
print(" ".join(res))
    