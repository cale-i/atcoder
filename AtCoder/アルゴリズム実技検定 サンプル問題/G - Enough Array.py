# 2019/11/25

n,k=map(int,input().split())
a=list(map(int,input().split()))

res=a[0]
r=1
ans=0
for l in range(n):
    while r<n and res<k:
        res+=a[r]
        r+=1
    if res>=k:
        ans+=n-r+1
    res-=a[l]

print(ans)