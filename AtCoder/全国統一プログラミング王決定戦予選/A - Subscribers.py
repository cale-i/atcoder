# 2019/11/30

n,a,b=map(int,input().split())
print(*[min(a,b),max(a+b-n,0)],sep=' ')