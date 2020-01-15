# 2020/01/15

import sys
from collections import Counter
input=sys.stdin.readline

n=int(input())
a=[int(input()) for _ in range(n)]
_set=set(range(1,n+1))
set_a=set(a)

if set_a==_set:
    print('Correct') 
    exit()

c=Counter(a).most_common(1)


x=(_set-set_a).pop()
y=c[0][0]
print(*[y,x])