# 2019/07/13

from heapq import heappop,heappush,heapify
import sys

input=sys.stdin.readline

n,k=map(int,input().split())
que=[]
for i in range(n):
    a,b=map(int,input().split())
    que.append((a,b))

heapify(que)

cnt=0
t=0
while cnt<k:
    a,b=heappop(que)
    t+=a
    cnt+=1
    hq=(a+b,b)
    heappush(que,hq)
print(t)
