# 2019/12/08

num=999
ans=0
for i in range(1,num+1):
    for j in range(1,num+1):
        s=str(i*j)
        if s==s[::-1]:
            ans=max(ans,i*j)
print(ans)