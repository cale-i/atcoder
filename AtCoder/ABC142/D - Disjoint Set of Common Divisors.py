# 2019/09/30

from fractions import gcd

a,b=map(int,input().split())

g=gcd(a,b)


def trial_div(n):
    from collections import Counter
    
    prime=Counter()

    for i in range(2,int(pow(n,0.5)+2)):
        while n%i==0:
            n//=i
            prime[i]+=1
    if n>1:prime[n]+=1
    
    return prime


res=trial_div(g)
print(1+len(res))