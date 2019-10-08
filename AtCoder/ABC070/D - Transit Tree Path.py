# 2019/07/12
# Dijkstra ver
# ダイクストラ

import sys
from heapq import heappop,heappush

input=sys.stdin.readline

n=int(input())
edge=[[] for _ in range(n)]
for _ in range(n-1):
    u,v,c=map(int,input().split())
    u-=1
    v-=1
    edge[u].append((c,v))
    edge[v].append((c,u))


def dijkstra(s):
    d=[float('inf')]*n
    visited=[False]*n
    d[s]=0
    visited[s]=True
    que=[]
    for e in edge[s]:
        heappush(que,e)
    while que:
        c,v=heappop(que)
        if visited[v]:continue
        d[v]=c
        visited[v]=True
        for cost,vtx in edge[v]:
            if visited[vtx]:continue
            hq=(cost+d[v],vtx)
            heappush(que,hq)

    return d

q,k=map(int,input().split())
k-=1

res=dijkstra(k)
for _ in range(q):
    x,y=map(int,input().split())
    x-=1
    y-=1
    print(res[x]+res[y])

# ******************************************************
# ******************************************************



# 2019/07/12
# DFS ver

import sys

sys.setrecursionlimit(10**9)
input=sys.stdin.readline

n=int(input())
edge=[[] for _ in range(n)]
for _ in range(n-1):
    u,v,c=map(int,input().split())
    u-=1 ; v-=1
    edge[u].append((c,v))
    edge[v].append((c,u))

q,k=map(int,input().split())
k-=1

d=[0]*n
visited=[False]*n

def dfs(s,p):
    visited[s]=True
    for c,v in edge[s]:
        if visited[v] or p==v:continue
        d[v]=c+d[s]
        visited[v]=True
        dfs(v,s)
    return 


dfs(k,-1)
for _ in range(q):
    x,y=map(int,input().split())
    x-=1 ; y-=1
    print(d[x]+d[y])

