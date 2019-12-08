# 2019/12/08

from collections import Counter
def trial_div(n):
    prime=Counter()
    for i in range(2,int(pow(n,0.5)+2)):
        while n%i==0:
            n//=i
            prime[i]+=1
    if n>1:prime[n]+=1
    return prime

num=20
c={}
for i in range(1,num+1):
    prime=trial_div(i)
    for p,v in prime.items():
        c[p]=max(c.get(p,1),v)

ans=1
for k,v in c.items():
    ans*=k**v
print(ans)