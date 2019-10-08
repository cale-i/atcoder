# 2019/07/25

n,k=map(int,input().split())
a=list(map(int,input().split()))

one=a.index(1)
ans=float('inf')

for i in range(k):
    l=one
    r=n-one-1

    l-=i
    r-=(k-i-1)
    ans=min(-(-l//(k-1))+-(-r//(k-1))+1,ans)

print(ans)