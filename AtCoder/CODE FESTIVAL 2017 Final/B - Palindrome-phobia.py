# 2019/09/27
"""
from collections import Counter
s=input()
n=len(s)
c=Counter(s)

res=c.values()
if len(res)<3:
    if n==len(res):
        print('YES')
    else:print('NO')
    exit()


if max(res)-min(res)>1 :
    print('NO')
else:
    print('YES')
"""

s=input()
a=s.count('a')
b=s.count('b')
c=s.count('c')

print('YES' if max(a,b,c)-min(a,b,c)<=1 else 'NO')