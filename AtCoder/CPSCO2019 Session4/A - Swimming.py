# 2019/07/18

l,x=map(int,input().split())
res=x%l
if x//l%2==0:ans=res
else:ans=l-res
print(ans)