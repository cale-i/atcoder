# Prim プリム法
# O(E log V) フィボナッチヒープ+隣接リストの場合

# 想定入力
"""
7 9
0 1 1
1 2 2
1 3 3
2 5 10
1 4 7
3 4 1
3 6 5
4 6 8
5 4 5

"""
# 想定出力
"""
17
[0, 1, 2, 3, 1, 5, 5]

"""


from heapq import heappush,heappop

n,m=map(int,input().split())
edge=[[] for _ in range(n)]
for _ in range(m):
    u,v,c=map(int,input().split())
    edge[u].append((c,v))
    edge[v].append((c,u)) # 無向グラフの場合


def prim(s):
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
            hq=(cost,vtx)
            heappush(que,hq)
    return d

start=0
res=prim(start)
print(sum(res))
print(res)
