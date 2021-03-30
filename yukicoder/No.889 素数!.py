# 2020/01/19

n=int(input())

if n<2:
    print(n)
    exit()

def divisors(n):
    div=[]
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            div.append(i)
            if i!=n//i:
                div.append(n//i)
    div.sort()
    return div

from collections import Counter

def trial_div(n):
    
    prime=Counter()

    for i in range(2,int(pow(n,0.5)+2)):
        while n%i==0:
            n//=i
            prime[i]+=1
    if n>1:prime[n]+=1
    
    return prime

div=divisors(n)

if len(div)==2:
    print('Sosu!')
    exit()

td=trial_div(n)


def check(n):
   return all(map(lambda x: x%n==0,td.values()))

if check(2):
    print('Heihosu!')
elif check(3):
    print('Ripposu!')
elif sum(div[:-1])==n:
    print('Kanzensu!')
else:
    print(n)
