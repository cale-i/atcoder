# 2019/08/10

n,m=map(int,input().split())

ans=max(n+m,n-m,n*m)
print(ans)