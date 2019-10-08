# 2019/08/10

from bisect import bisect_left

n,k=map(int,input().split())
x=list(map(int,input().split()))

idx=bisect_left(x,0)
rn=n-idx
l=idx if rn>=k else idx-(k-rn)
r=l+k-1
ans=float('inf')

while 0<=l and idx<=r+1:
    if idx==l and r-l+2>=k:
        lf=float('inf')
        rf=x[r]
    elif idx==r+1 and r-l+2>=k:
        lf=abs(x[l])
        rf=float('inf')
    else:
        lf=abs(x[l])*2+x[r] 
        rf=x[r]*2+abs(x[l])
    ans=min(min(lf,rf),ans)

    l-=1;r-=1
print(ans)