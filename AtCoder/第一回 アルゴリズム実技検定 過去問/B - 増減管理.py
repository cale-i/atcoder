# 2020/01/15

import sys
input=sys.stdin.readline

n=int(input())
a=[int(input()) for _ in range(n)]

for i in range(1,n):    
    dif=a[i]-a[i-1]
    if dif>0:
        res=['up',dif]
    elif dif<0:
        res=['down',-dif]
    else:
        res=['stay']
    print(*res)