# 2019/07/06

import sys

input=sys.stdin.readline

n=int(input())
s={}
for i in range(n):
    tmp=input()
    if tmp[0] in ['M','A','R','C','H']:
        s[tmp[0]]=s.get(tmp[0],0)+1

# ↑ここまでできた
# ↓ここからわからん

ans=0
for ik,iv in s.items():
    for jk,jv in s.items():
        if ik==jk:break
        for kk,kv in s.items():
            if jk==kk:break
            ans+=iv*jv*kv

print(ans)


# 2019/07/06
# ref #6111591

import sys
from itertools import combinations
input=sys.stdin.readline

n=int(input())
s={}
for i in range(n):
    tmp=input()[0]
    if tmp in ['M','A','R','C','H']:
        s[tmp]=s.get(tmp,0)+1

ans=0

cmb=list(combinations(s.values(),3))

for a,b,c in cmb:
    ans+=a*b*c

print(ans)

