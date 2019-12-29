# 2019/12/29
# BFS

from collections import deque

n=int(input())


def bfs(s,g):
    visited=[False]*(n+1)
    d=[-1]*(n+1)
    d[s]=1
    visited[0]=True
    visited[s]=True
    que=deque()
    que.append(s)

    while que:
        u=que.popleft()
        step=bin(u).count('1')
        nxt=u+step
        prv=u-step

        for v in [nxt,prv]:
            if v>n:continue
            if visited[v]:continue
            visited[v]=True
            d[v]=d[u]+1
            que.append(v)
            
        

    return d

res=bfs(1,n)
print(res[n])