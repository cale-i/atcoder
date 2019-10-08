"""import sys
from collections import Counter
input=sys.stdin.readline

n,k,q=map(int,input().split())
a=Counter([int(input()) for _ in range(q)])

ans=[False]*n
for key,v in a.items():
    if k-(q-v)>0:
        ans[key-1]=True

ss=set(a.keys())

for i in range(n):
    if i+1 in ss:continue
    if k-q>0:
        ans[i]=True
    


for e in ans:
    if e:
        print('Yes')
    else:
        print('No')

"""
# 2019/09/16
# 解説のやつ
import sys
input=sys.stdin.readline

n,k,q=map(int,input().split())
res=[k-q]*n

for i in range(q):
    res[int(input())-1]+=1

for e in res:
    print('Yes' if e>0 else 'No')