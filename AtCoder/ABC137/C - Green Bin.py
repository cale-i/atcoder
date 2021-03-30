# 2019/08/10

import sys
input=sys.stdin.readline
from collections import Counter

n=int(input())
s=[]
for i in range(n):
    a=sorted(list((input().rstrip('\n'))))
    a=''.join(a)
    s.append(a)
c=Counter(s)

cnt=0
for k,v in c.items():
    if v>1:
        cnt+=v*(v-1)//2

print(cnt)