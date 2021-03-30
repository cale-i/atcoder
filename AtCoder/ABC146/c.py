# 2019/11/24

a,b,x=map(int,input().split())
ans=0
for disit in range(1,19):
    n=(x-b*disit)//a
    if a*n+b*len(str(n))<=x:
        ans=max(ans,n)
ans=min(ans,1000000000)
print(ans)