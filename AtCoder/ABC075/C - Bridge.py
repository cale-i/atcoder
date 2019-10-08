# 2019/07/16

from heapq import heappop,heappush

n,m=map(int,input().split())
edge=[[] for _ in range(n)]
del_edge=[]
cnt=0

for _ in range(m):
    a,b=map(int,input().split())
    a-=1;b-=1
    edge[a].append(b)
    edge[b].append(a)
    del_edge.append((a,b))


def find(s,de):
    visited=[False]*n
    visited[s]=True
    que=[]
    for e in edge[s]:
        if s in de and e in de:continue
        heappush(que,e)
    while que: 
        v=heappop(que)
        if visited[v]:continue
        visited[v]=True
        for vtx in edge[v]:
            if v in de and vtx in de:continue
            if visited[vtx]:continue
            hq=vtx
            heappush(que,hq)

    if False in visited:
        return 1
    else:return 0

for i in range(m):
    tmp=del_edge[i]
    cnt+=find(0,tmp)

print(cnt)

