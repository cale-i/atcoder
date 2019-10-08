# 2019/09/09

from collections import deque

h,w=map(int,input().split())
n=int(input())
a=list(map(int,input().split()))

res=[]
for i in range(n):
    res+=[i+1]*a[i]

res=deque(res)

for i in range(h):
    tmp=[]
    for j in range(w):
        tmp.append(res.popleft())
    if i%2:print(*tmp[::-1])
    else:print(*tmp)