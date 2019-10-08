# 2019/08/07

from fractions import gcd

n,X=map(int,input().split())
x=list(map(int,input().split()))
x.append(X)
x.sort()
g=0
for i in range(n):
    g=gcd(g,x[i+1]-x[i])
print(g)