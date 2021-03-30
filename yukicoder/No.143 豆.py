# 2019/12/28

k,n,f=map(int,input().split())
a=list(map(int,input().split()))
res=k*n-sum(a)
print(max(res,-1))