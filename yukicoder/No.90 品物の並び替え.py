# 2019/12/31
# python3ではTLE

from itertools import permutations

n,m=map(int,input().split())
items=[tuple(map(int,input().split())) for _ in range(m)]
ps=list(permutations(range(n),n))

ans=0
for p in ps:
    cnt=0
    pp=[None]*n
    for i in range(n):
        pp[p[i]]=i

    for item in items:
        u,v,c=item
        if pp[u]<pp[v]:
            cnt+=c
    ans=max(ans,cnt)
print(ans)