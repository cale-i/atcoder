# 2019/12/29
# メモ化

from collections import deque

n=int(input())

def sieve(n):
    end=int(pow(n,0.5))+1
    is_prime=[True]*(n+1)
    is_prime[0]=False
    is_prime[1]=False

    for i in range(2,end+1):
        if not is_prime[i]:continue
        for j in range(i*2,n+1,i):
            is_prime[j]=False
    return [i for i in range(n+1) if is_prime[i]]

primes=deque(sieve(n))
memo=[False]*(n+1)
que=[]

p=primes.popleft()
for i in range(2,n+1):
    while p<=i:
        que.append(p)
        if primes:
            p=primes.popleft()
        else:
            p=float('inf')
            break
    for e in que:
        if i-e<2:memo[i]|=False
        else:memo[i]|=not memo[i-e]
        if memo[i]:break

print('Win' if memo[n] else 'Lose')