# 2019/11/9
# だめだった

mod=998244353
n=int(input())
d=list(map(int,input().split()))

if d[0]!=0:
    print(0)
    exit()

res={}
for e in d:
    res[e]=res.get(e,0)+1

if res[0]>1:
    print(0)
    exit()

def cmb(n,r,mod):
    global memo
    fac=[1,1]
    for i in range(2,n+1):
        fac.append(fac[i-1]*i%mod)
    ret=fac[n]*pow(fac[r]*fac[n-r]%mod,mod-2,mod)%mod
    return ret


ans=1
pre=res.get(1,-1)
if pre==-1:
    print(0)
    exit()

memo={}

cnt=0
for i in range(2,len(res)):
    tmp=res.get(i,-1)
    if tmp==-1:
        print(0)
        exit()
    j=1
    while j<=(tmp-1)//2:
        cnt+=cmb(tmp,j,mod)*2
        j+=1
    if tmp%2==0:
        cnt+=cmb(tmp,tmp//2,mod)
    cnt+=pre
    ans=(ans%mod)*(cnt%mod)
    cnt=0
    pre=tmp
print(ans)