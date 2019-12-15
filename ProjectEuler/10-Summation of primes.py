# 2019/12/10

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
    return sum([i for i in range(n+1) if is_prime[i]])

n=2_000_000
print(sieve(n))