# 2019/12/27

from heapq import heapify,heappop,heappush
import sys

input=sys.stdin.readline
n,m=map(int,input().split())
ab=[[] for _ in range(m+1)]

for i in range(n):
    a,b=map(int,input().split())
    if a>m:continue
    ab[a].append(-b)

que=[]
heapify(que)
ans=0
for i in range(1,m+1):
    if ab[i]:
        for e in ab[i]:
            heappush(que,e)
    if que:
        ans+=heappop(que)

print(-ans)