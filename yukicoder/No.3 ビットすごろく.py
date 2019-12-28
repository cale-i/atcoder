# 2019/12/28

from heapq import heappop,heappush

n=int(input())

edge=[[] for _ in range(n+1)]
for i in range(n+1):
    u,v=i,i+bin(i).count('1')
    if v<=n:
        edge[u].append((u,v))
    u,v=i,i-bin(i).count('1')
    if v>0:
        edge[u].append((u,v))


def dijkstra(p,s):
    d=[float('inf')]*(n+1)
    d[s]=1
    que=[]
    for e in edge[s]:
        heappush(que,e)
    while que:
        p,v=heappop(que)
        if d[v]<=d[p]+1:continue
        d[v]=d[p]+1
        for pp,vtx in edge[v]:
            if d[vtx]<=d[pp]+1:continue
            hq=(pp,vtx)
            heappush(que,hq)
    return d


res=dijkstra(0,1)
print(res[n] if res[n]!=float('inf') else -1)