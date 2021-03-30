# 2019/11/29
from collections import Counter

n,p=map(int,input().split())
def trial_div(n):
    
    prime=Counter()

    for i in range(2,int(pow(n,0.5)+2)):
        while n%i==0:
            n//=i
            prime[i]+=1
    if n>1:prime[n]+=1
    
    return prime


prime=trial_div(p)
if prime is None:
    print(1)
    exit()
ans=1
for k,v in prime.items():
    if v>=n:
        ans*=k**(v//n)
print(ans)