# 2019/06/05
# ワーシャルフロイド
# froyd warshall

from scipy.sparse.csgraph import floyd_warshall
n,m=map(int,input().split())

d=[[0 for i in range(n)] for j in range(n)]

for i in range(m):
    u,v,c=map(int,input().split())
    d[u-1][v-1]=d[v-1][u-1]=c

dd=floyd_warshall(d)

ans=float('inf')
for e in dd:
    ans=min(ans,max(e))
print(int(ans))