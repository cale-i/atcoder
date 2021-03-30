# 2019/08/19

n,k=map(int,input().split())
a=list(map(int,input().split()))

l=0
r=k
res=sum(a[:k])
ans=res
while r<n:
    res-=a[l]
    res+=a[r]
    r+=1
    l+=1
    ans+=res
    
print(ans)