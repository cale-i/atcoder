# 2019/12/28

l=int(input())
m=int(input())
n=int(input())
ans=0

div,mod=divmod(n,25)
ans+=mod
div,mod=divmod(m+div,4)
ans+=mod
div,mod=divmod(l+div,10)
ans+=mod
print(ans)