# 2019/07/23

# ↓MLEでるやつ
"""
input=open(0).readline
n,k=map(int,input().split())
res=[]
for i in range(n):
    a,b=map(int,input().split())
    res+=[a]*b
res.sort()
print(res[k-1])

"""
# AC

from heapq import heappop,heappush

input=open(0).readline
n,k=map(int,input().split())
res={}
for i in range(n):
    a,b=map(int,input().split())
    res[a]=res.get(a,0)+b

que=[]
for key,val in res.items():
    heappush(que,(key,val))

while k:
    key,val=heappop(que)
    if val>=k:
        print(key)
        exit()
    k-=val
