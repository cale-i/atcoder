# 2019/11/25

from heapq import heapify,heappop,heappush

n,m=map(int,input().split())
que=list(map(lambda x: -int(x),input().split()))
heapify(que)
for _ in range(m):
    q=heappop(que)
    if q==0:break
    heappush(que,-(-q//2))
print(-sum(que))