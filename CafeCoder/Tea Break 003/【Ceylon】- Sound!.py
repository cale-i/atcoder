# 2019/12/30

n,k=map(int,input().split())
a=sorted(map(int,input().split()))
if k<=a[0]:
    ans=a[-1]-k
elif k>=a[-1]:
    ans=k-a[0]
else:ans=k-a[0]+a[-1]-k
print(ans)