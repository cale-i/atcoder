# 2019/07/17

from heapq import heappop,heappush

k,t=map(int,input().split())
a=list(map(int,input().split()))
que=[]
for i in range(t):
    hq=(-a[i],i)
    heappush(que,hq)

pre_v,pre_idx=heappop(que)
hq=(pre_v+1,pre_idx)
heappush(que,hq)

cnt=0

for i in range(k-1):
    v,idx=heappop(que)
    if idx==pre_idx :
        if que:
            hq=(v,idx)
            v,idx=heappop(que)
            heappush(que,hq)    
        else:
            cnt+=-v
            break
    v+=1
    hq=(v,idx)
    pre_v,pre_idx=hq
    if v==0:continue
    heappush(que,hq)

print(cnt)

# O(1)
k,t=map(int,input().split())
a=list(map(int,input().split()))

max_a=max(a)
print(max(max_a-(k-max_a)-1,0))
