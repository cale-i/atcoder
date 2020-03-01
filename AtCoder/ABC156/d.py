MOD=10**9+7

n,a,b=map(int,input().split())
com=[]
ans=pow(2,n,MOD)-1


def cmb(k):
    ret=1
    x,y=1,1
    for i in range(1,k+1):
        x*=(n-i+1)%MOD
        x%=MOD
        y*=i
        y%=MOD
    ret=x*pow(y%MOD,MOD-2,MOD)%MOD

    return ret%MOD



ans-=(cmb(a)+cmb(b))%MOD
print(ans)