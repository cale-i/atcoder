from heapq import heappop,heappush,heapify

n,m=map(int,input().split())

que=list(map(lambda x: -int(x),input().split()))
heapify(que)

while m:
    res=-heappop(que)
    res>>=1
    heappush(que,-res)
    m-=1

print(-sum(que))