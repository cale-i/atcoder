# Dijkstra ダイクストラ
# O(|E+V|log E)

# 想定入力
"""
7 10
0 1 2
0 2 5
1 2 4
2 3 2
1 3 6
1 4 10
3 5 1
4 5 3
4 6 5
5 6 9

"""
# 想定出力
"""
[0, 2, 5, 7, 11, 8, 16]
"""

from heapq import heappop,heappush

n,m=map(int,input().split())
edge=[[] for _ in range(n)]

for _ in range(m):
    u,v,c=map(int,input().split())
    edge[u].append((c,v))
    edge[v].append((c,u)) # 無向グラフの場合


def dijkstra(s):
    d=[float('inf')]*n
    visited=[False]*n
    d[s]=0          #スタート位置のコストを0で初期化
    visited[s]=True #スタート位置を訪問済みにする
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
