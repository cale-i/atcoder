mod=10**9+7
n,k=map(int,input().split())
a=list(map(int,input().split()))
kk=k-1

cnt=0
res=0
for i in range(n):
    cnt=0
    rev=0

    for j in range(i+1,n):
        if a[i]>a[j]:
            cnt+=1
        if a[i]<a[j]:
            rev+=1
    res+=rev*((kk+1)*kk)//2
    res+=cnt*((k+1)*k)//2
    res%=mod

print(res)