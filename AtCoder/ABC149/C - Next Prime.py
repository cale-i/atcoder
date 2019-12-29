# 2019/12/29

from bisect import bisect_left

x=int(input())

def sieve(n):
    end=int(pow(n,0.5))+1
    is_prime=[True]*(n+1)
    is_prime[0]=False
    is_prime[1]=False

    for i in range(2,end+1):
        if not is_prime[i]:continue
        for j in range(i*2,n+1,i):
        #for j in range(i*(i|0),n+1,i):
            is_prime[j]=False
    return [i for i in range(n+1) if is_prime[i]]

primes=sieve(10**5+10)
ans=bisect_left(primes,x)
print(primes[ans])