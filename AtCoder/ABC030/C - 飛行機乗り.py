# 2019/07/16

import bisect

n,m=map(int,input().split())
x,y=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

cnt=0

at=bt=0
while True:
    bt=a[at]+x
    tmp=bisect.bisect_left(b,bt)
    if tmp>=m:break
    bt=tmp

    at=b[bt]+y
    tmp=bisect.bisect_left(a,at)
    cnt+=1
    if tmp>=n:break
    at=tmp

print(cnt)