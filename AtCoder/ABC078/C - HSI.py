# 2019/08/08

n,m=map(int,input().split())

a=(n-m)*100*2**m
b=1900*(2**m)*m
print(a+b)