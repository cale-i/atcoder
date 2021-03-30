n,k=map(int,input().split())
p=list(map(int,input().split()))

res=[]
for i in range(n):
    tmp=((p[i]*(p[i]+1))//2)/p[i]
    res.append(tmp)

ans=sum(res[:k])
ret=ans
for i in range(n-k):
    ret+=res[i+k]-res[i]
    ans=max(ret,ans)

print(ans)