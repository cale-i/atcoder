# 2019/12/30

n,q=map(int,input().split())
a=list(map(int,input().split()))
aa=[0]*(10**5+1)

for e in a:
    aa[e]+=1

for i in range(q):
    x,y=map(int,input().split())
    aa[y]+=aa[x]
    aa[x]=0

ans=0
for i in range(1,len(aa)):
    ans+=i*aa[i]
print(ans)

