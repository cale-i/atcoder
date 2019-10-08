# 2019/08/12
from math import factorial

n=int(input())
mod=(10**9+7)
def trial_div(n):
    div={}
    for i in range(2,n+1):
        res=i
        for j in range(2,i+1):
            while res%j==0:
                res//=j
                div[j]=div.get(j,0)+1
    return div

res=trial_div(n)
ans=1
for k,v in res.items():
    ans=(ans*(v+1))%mod
print(ans)
