# 2019/07/30
# コーナーケース引っかかりすぎ

n,m,k,e=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a.sort()
b.sort(reverse=True)

ans=0
cnt=0
i=0
j=0
while i<k:
    if e<a[j]:
        cnt+=1
        e+=b[i]
        i+=1
    while e-a[j]>=0 or j==0:
        if j==0 and e<a[j]:break
        e-=a[j]
        ans+=1
        j+=1
        if j==n:break
    if j==n:break
else:
    print('No')
    print(ans)
    exit()
print('Yes')
print(cnt)