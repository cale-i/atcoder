# 2019/11/9

import sys
input=sys.stdin.readline

n,k=map(int,input().split())
a=[int(input()) for _ in range(n)]
i=0
cnt=1
ans=0
while i<n-1:
    if a[i]<a[i+1]:
        cnt+=1
        i+=1
        continue
    if cnt>=k:
        ans+=cnt-k+1
    cnt=1
    i+=1
if cnt>=k:
    ans+=cnt-k+1
print(ans)