# 2019/08/09

from collections import Counter
s=list(input())
n=len(s)
S=set(s)
"""
if len(s)==len(S):
    print(n//2)
    exit()"""
if s.count(s[0])==len(s):
    print(0)
    exit()


res=float('inf')
for e in S:
    r=0
    l=0
    cnt=0
    
    while l<=r<n:
        if s[r]==e:
            if l==0:
                cnt=max(r-l,cnt)
            else:
                cnt=max(r-l-1,cnt)
            l=r
        r+=1
    if n==r:cnt=max(r-l-1,cnt)
    if cnt==0:continue
    res=min(res,cnt)
if res==float('inf'):
    print(0)
else:print(res)