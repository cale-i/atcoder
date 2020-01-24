# yukicoder No.713 素数の和 2020/01/24

def sieve(n):
    if n<2:return [0]
    end=int(pow(n,0.5))+1
    is_prime=[True]*(n+1)
    is_prime[0]=False
    is_prime[1]=False

    for i in range(2,end+1):
        if not is_prime[i]:continue
        for j in range(i*2,n+1,i):
            is_prime[j]=False
    return [i for i in range(n+1) if is_prime[i]]

n=int(input())
ans=sum(sieve(n))
print(ans)