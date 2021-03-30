# Union-Find
# Disjoint-Set

class unionfind():
    def __init__(self,n):
        self.par=list(range(n+1))
        self.rank=[0]*(n+1)
        self.groups=n # 連結成分の個数
    
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
        if x!=y:self.groups-=1 # 連結成分の個数

 
c=unionfind(10)
print(c)