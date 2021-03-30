# 2019/08/08

# from fractions import gcd
from math import gcd
n=int(input())
a=list(map(int,input().split()))

res=0
for i in range(n):
    res=gcd(res,a[i])

print(res)