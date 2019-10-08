# 2019/08/15

from fractions import gcd

n,k=map(int,input().split())
a=list(map(int,input().split()))
ans='POSSIBLE'
max_a=max(a)
if max_a==k:
    print(ans)
    exit()
elif max_a<k:
    print('IMPOSSIBLE')
    exit()

    

g=0
for i in range(n):
    g=gcd(g,a[i])

if k%g==0 or k in a:
    print(ans)
else:
    print('IMPOSSIBLE')