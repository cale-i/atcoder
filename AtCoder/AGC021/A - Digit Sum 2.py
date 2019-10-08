# 2019/08/06

n=list(map(int,list(input())))
ans=sum(n)
if ans!=n[0]+9*(len(n)-1):
    ans=n[0]-1+9*(len(n)-1)

print(ans)