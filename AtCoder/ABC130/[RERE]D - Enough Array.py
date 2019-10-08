# 2019/07/12

n,k=map(int,input().split())
a=list(map(int,input().split()))

r=0
cnt=0
res=0
for l in range(n):
    while r<n and cnt<k:
        cnt+=a[r]
        r+=1

    if cnt>=k:res+=n-r+1
    if r==l:r+=1
    else:cnt-=a[l]

print(res)