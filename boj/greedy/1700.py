import sys
input = sys.stdin.readline
INF = int(1e9)
count = 0
n,k = map(int,input().split())
datas = list(map(int,input().split()))
nxt_idx_list = []

for i in range(len(datas)):
    now_num = datas[i]
    nxt_idx = INF
    for j in range(i+1,len(datas)):
        
        if now_num == datas[j]:
            nxt_idx = j
            break
    
    nxt_idx_list.append([now_num,nxt_idx])

concent = []   ## (number,nxt_idx)
in_concent = [] ## number 

concent.append(nxt_idx_list[0])
in_concent.append(nxt_idx_list[0][0])
nxt_idx_list = nxt_idx_list[1:]
concent = sorted(concent,key=lambda x:-x[1])


for i in range(len(nxt_idx_list)):

    new_num, nxt_idx = nxt_idx_list[i]
    if new_num in in_concent:
        
        for i in range(len(concent)):
            if concent[i][0] == new_num:
                concent[i][1] = nxt_idx
                concent = sorted(concent,key=lambda x:-x[1])
                break

        continue
    
    if new_num not in concent and len(concent) < n:
        in_concent.append(new_num)
        concent.append([new_num,nxt_idx])
      
        continue
    
    concent = sorted(concent, key= lambda x:-x[1])
    in_concent.append(new_num)
    in_concent.remove(concent[0][0])
    concent[0][0] = new_num
    concent[0][1] = nxt_idx
    count += 1

print(count)      
