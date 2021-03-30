# Dijkstra

from heapq import heappop,heappush

n,m=map(int,input().split())
edge=[[] for _ in range(n)]
for _ in range(m):
    u,v,c=map(int,input().split())
    #u-=1;v-=1
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


res=dijkstra(0)
print(res)