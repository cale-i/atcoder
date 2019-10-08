#%%
#2019/07/21

n=int(input())
a=[-1]+list(map(int,input().split()))

b=[-1]*(n+1)

bgn=n//2+1

for i in range(bgn,n+1):
    b[i]=a[i]

for i in range(bgn-1,0,-1):
    j=i
    cnt=0
    while j<=n:
        cnt+=a[j]
        j+=i
    res=cnt%2
    if res==a[i]:b[i]=a[i]
    else:b[i]=1

if b.count(1)>0:
    print(len(b)-1)
    print(*b[1:])
else:print(0)

#%%
# 2019/10/04

n=int(input())
a=[0]+list(map(int,input().split()))
b=[0]+[0]*n

for i in range(n):
    idx=n-i
    j=2
    cnt=0
    while idx*j<=n:
        cnt+=b[idx*j]
        j+=1
    cnt%=2
    if cnt==a[idx]:continue
    b[idx]=1
    
smb=sum(b)
print(smb)
for i in range(1,n+1):
    if b[i]:print(i,end=' ')
if smb:print()



#%%
