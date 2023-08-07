import sys
input = sys.stdin.readline
dic = ['c=','c-','dz=','d-','lj','nj','s=','z=']
count = 0
data = input().strip()

for m in dic:
    if m in data:

        data = data.split(m)
      
        count += len(data)-1
        data = "/".join(data)
    


tmp = data.split("/")
tmp = "".join(tmp)


count += len(tmp)
print(count)