# 2019/07/18
"""
from collections import deque

n,d=map(int,input().split())
R=list(map(int,input().split()))
R.sort()
r=0
res=0
for l in range(n): 
    while r<n-1 and R[r]-R[l]<=d:
        r+=1

    if r-l>=3:
        res+=
    if R[r]-R[l]<=d:
        res+=cnt-2
    if l==r-1:r+=1
    else:cnt-=1
    
print(res)
"""
# 2019/07/18
# だめだめ

from collections import deque

n,d=map(int,input().split())
R=list(map(int,input().split()))
R.sort()
r=0
res=0
for l in range(n): 
    while r<n and R[r]-R[l]<=d:
        r+=1
    if r-l>=3:
        res+=(r-l-1)*(r-l-2)//2  # ここがわからんかった
    if l==r:r+=1
    
print(res)
