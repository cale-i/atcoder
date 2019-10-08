# 2019/07/14

import sys
input=sys.stdin.readline


class unionfind():
    def __init__(self,n):
        self.par=list(range(n+1))
        self.rank=[0]*(n+1)
    def find(self,x):
        if self.par[x]==x:
            return x
        else:
            self.par[x]=self.find(self.par[x])
            return self.par[x]
    def is_same(self,x,y):
        return self.find(x)==self.find(y)
    def unite(self,x,y):
        x=self.find(x)
        y=self.find(y)
        if self.rank[x]<self.rank[y]:
            self.par[x]=y
        else:
            self.par[y]=x
            if self.rank[x]==self.rank[y]:
                self.rank[x]+=1


n,q=map(int,input().split())
uf=unionfind(n)
ans=[]
for i in range(q):
    p,a,b=map(int,input().split())
    if p==0:
        uf.unite(a,b)

    else:
        res=uf.is_same(a,b)
        ans+=['Yes' if res else 'No']

print(*ans,sep='\n')