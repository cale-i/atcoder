# 2019/07/12

from fractions import gcd

n=int(input())
l=1
for _ in range(n):
    tmp=int(input())
    l=(tmp*l)//gcd(tmp,l)
print(l)
