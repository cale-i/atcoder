# 2019/12/08
from collections import Counter

num=600_851_475_143

def trial_div(n):
    prime=Counter()
    for i in range(2,int(pow(n,0.5)+2)):
        while n%i==0:
            n//=i
            prime[i]+=1
    if n>1:prime[n]+=1
    return prime


print(max(trial_div(num)))