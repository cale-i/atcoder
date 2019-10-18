# 2019/09/28
from fractions import gcd

a,b=map(int,input().split())


# 約数列挙

def divisors(n):
    div=[]
    if n%2==0:div.append(2)
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            if i%2:
                div.append(i)
                if i!=n//i and n//i%2:
                    div.append(n//i)
    # div.sort()
    return div

diva=divisors(a)
divb=divisors(b)
div=set()
for aa,bb in zip(diva,divb):
    if aa in divb:
        div.add(aa)
    if bb in diva:
        div.add(bb)



def sieve(n):
    end=int(pow(n,0.5))+1
    is_prime=[True]*(n+1) 
    is_prime[0]=False
    is_prime[1]=False

    for i in range(2,end):
        if not is_prime[i]:continue
        for j in range(i*2,n+1,i):
        #for j in range(i*(i|0),n+1,i):
            is_prime[j]=False
    return [i for i in range(n+1) if is_prime[i]]


cnt=1

prime=sieve(max(div))

for e in div:
    if e in prime:
        cnt+=1
print(cnt)