# 2019/11/16

import math
mod=10**9+7
X,Y=map(int,input().split())

x=(2*X-Y)/3
y=X-2*x
if x!=int(x) or y!=int(y):
    print(0)
    exit()
else:
    x=int(x)
    y=int(y)

def cmb(n,r,mod=10**9+7):
    fac=[1,1]
    for i in range(2,n+1):
        fac.append(fac[i-1]*i%mod)
    ret=fac[n]*pow(fac[r]*fac[n-r]%mod,mod-2,mod)%mod
    return ret

if x<0 or y<0:
    print(0)
    exit()

n=x+y
r=min(x,y)

ans=cmb(n,r)
if x==0:
    if Y==2*y and X==Y//2:
        print(ans)
    else:print(0)
elif y==0:
    if X==2*x and Y==X//2:
        print(ans)
    else:print(0)
else:
    print(ans)

