# 2019/10/16
# だめ

import sys
input=sys.stdin.readline

n=int(input())
a=sorted([int(input()) for _ in range(n)])

l,r=1,n-2
L=a[0]
R=a[-1]
cnt=abs(L-R)

while l<=r:
    
    ll=abs(L-a[l])
    lr=abs(L-a[r])
    rl=abs(R-a[l])
    rr=abs(R-a[r])
    cnt+=max(ll,lr,rl,rr) 
    if max(ll,lr)<max(rl,rr):
        R=R-max(rl,rr) if R>max(rl,rr) else R+max(rl,rr)
        if rl>rr:l+=1
        else:r-=1
    else:
        L=L-max(ll,lr) if L>max(ll,lr) else L+max(ll,lr)
        if ll>lr:l+=1
        else:r-=1
print(cnt)