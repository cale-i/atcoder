# 2019/10/10
# 解答かんにんぐ
# 前回WAの原因は、u,vのいずれかが訪問済みである必要があった。
# edge参照順序によっては、u,vのいずれも未訪問となり、このときWAとなる。

import sys
sys.setrecursionlimit(10**7)

n=int(input())
node=[None]*n
edge=[[] for _ in range(n)]


for i in range(n-1):
    u,v,w=map(int,input().split())
    u-=1;v-=1
    edge[u].append((v,w))
    edge[v].append((u,w))


def dfs(v,p,c):
    node[v]=c
    for vv,w in edge[v]:
        if vv==p:continue
        dfs(vv,v,1-c) if w%2 else dfs(vv,v,c)


dfs(0,-1,0)

for e in node:
    print(e)