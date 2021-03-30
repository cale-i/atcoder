# 2019/09/04

w,h=map(int,input().split())
w-=1;h-=1
n=w+h
r=min(w,h)

class Combination():
    def __init__(self,n,mod=10**9+7):
        self.fac=[1,1]
        self.finv=[1,1]
        self.inv=[0,1]

        for i in range(2,n+1):
            self.fac.append(self.fac[i-1]*i%mod)
            self.inv.append(mod-self.inv[mod%i]*(mod//i)%mod)
            self.finv.append(self.finv[i-1]*self.inv[i]%mod)        

    def com(self,n,r,mod=10**9+7):
        if n<r:return 0
        if n<0|r<0:return 0
        return self.fac[n]*(self.finv[r]*self.finv[n-r]%mod)%mod
    


C=Combination(n)
print(C.com(n,r))

# 2019/09/04
# フェルマーの小定理ver

w,h=map(int,input().split())
w-=1;h-=1
n=w+h

mod=10**9+7

fac=[1,1]
for i in range(2,n+1):
    fac.append(fac[i-1]*i%mod)

l=fac[n]
r=pow((fac[w]*fac[h])%mod,mod-2,mod)
print(l*r%mod)

# ライブラリ使用

w,h=map(int,input().split())

def cmb(n,r,mod=10**9+7):
    fac=[1,1]
    for i in range(2,n+1):
        fac.append(fac[i-1]*i%mod)
    ret=fac[n]*pow(fac[r]*fac[n-r]%mod,mod-2,mod)%mod
    return ret

n=w+h-2
r=min(w,h)-1
print(cmb(n,r))