# 2019/07/25

from heapq import heappop,heappush,heapify

input=open(0).readline
n,m=map(int,input().split())

que=[]
for i in range(n):
    que.append(tuple(map(int,input().split())))
heapify(que)

cnt=0
rem=m
while rem:
    a,b=heappop(que)
    c=min(b,rem)
    cnt+=a*c
    rem-=c

print(cnt)