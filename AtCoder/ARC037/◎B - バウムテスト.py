# 2019/06/27

import sys
sys.setrecursionlimit(10**6)

n,m=map(int,input().split())

visited=[False]*n
adj={}
for i in range(n):
    adj[i]=[]
res=0

for i in range(m):
    u,v=map(int,input().split())
    u-=1
    v-=1
    if adj.get(u,0):
        adj[u]+=[v]
        adj[v]+=[u]
    else:
        adj[u]+=[v]
        adj[v]+=[u]

def dfs(u,p):
    visited[u]=True
    cycle=False
    for v in adj[u]:
        if v!=p:
            if visited[v]:return True
            cycle|=dfs(v,u)
    return cycle

res=0

for i in range(n):
    if visited[i]:continue
    c_cycle=dfs(i,-1)
    if not c_cycle:res+=1

print(res)
