# 2019/12/08

num=100
ans=0
for i in range(1,num+1):
    ans+=i**2
ans-=(num*(num+1)//2)**2
print(-ans)