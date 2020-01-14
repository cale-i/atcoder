# 2020/01/12

n,k,m=map(int,input().split())
a=list(map(int,input().split()))

tmp=n*m-sum(a)
if tmp>k:print(-1)
else:print(max(tmp,0))