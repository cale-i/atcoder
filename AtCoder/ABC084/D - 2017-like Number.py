# 2019/09/06

input=open(0).readline
q=int(input())

lr=[]
mxr=0

for i in range(q):
    l,r=map(int,input().split())
    lr.append((l,r))
    mxr=max(mxr,r)

def sieve(n):
    end=int(pow(n,0.5))+1
    is_prime=[True]*(n+1)
    is_prime[0]=False
    is_prime[1]=False

    for i in range(2,end+1):
        if not is_prime[i]:continue
        for j in range(i*2,n+1,i):
            is_prime[j]=False
    return is_prime

prime=sieve(mxr)

x=[0]
cnt=0
for i in range(1,mxr+1):
    if prime[i]&prime[(i+1)//2]:
        cnt+=1
    x.append(cnt)
for l,r in lr:
    print(x[r]-x[l-1])

