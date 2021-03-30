# 2019/07/20

from heapq import heappop,heappush,heapify

n,m=map(int,input().split())
a=list(map(int,input().split()))
heapify(a)
bc=[]
for i in range(m):
    b,c=map(int,input().split())
    hq=(-c,b)
    heappush(bc,hq)



def cg(res):

    while bc:
        c,b=heappop(bc)
        c=-c
        while b and a:
            b-=1
            v=heappop(a)
            if c>v:res+=c
            else:
                res+=v
                return res
    return res
res=0
res=cg(res)
print(sum(a)+res)