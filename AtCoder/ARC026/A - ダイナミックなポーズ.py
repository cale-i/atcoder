# 2019/10/31

n,a,b=map(int,input().split())
ans=max(0,(n-5))*a+min(n,5)*b
print(ans)