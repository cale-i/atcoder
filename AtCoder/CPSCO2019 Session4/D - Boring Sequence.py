# 2019/07/19

from heapq import heappop,heappush,heapify

n,k=map(int,input().split())
a=list(map(int,input().split()))+[-1]
cnt=1
que=[]
for i in range(1,n+1):
    if a[i]==a[i-1]:
        cnt+=1
    else:
        hq=(-cnt,cnt,1)
        heappush(que,hq)
        cnt=1

for i in range(k):
    now,org,cnt=heappop(que)
    cnt+=1
    now=org//cnt
    hq=(-now,org,cnt)
    heappush(que,hq)
ans=heappop(que)[0]
print(max(-ans,1))
