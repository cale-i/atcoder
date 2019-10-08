# 2019/07/09
# 帰路の考え方 かんにんぐ
# 逆向きに辿る => edge2
# Dijkstra ダイクストラ

from heapq import heappop,heappush

n,m,t=map(int,input().split())
A=list(map(int,input().split()))

edge1=[[] for i in range(n)]
edge2=[[] for i in range(n)]
for i in range(m):
    u,v,c=map(int,input().split())
    u-=1
    v-=1
    edge1[u].append((c,v))
    edge2[v].append((c,u))


def dijkstra(s,edge):
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


res1=dijkstra(0,edge1)
res2=dijkstra(0,edge2)

ans=float('-inf')
for i in range(n):
    time=t-(res1[i]+res2[i])
    ans=max(ans,A[i]*time)

print(ans)