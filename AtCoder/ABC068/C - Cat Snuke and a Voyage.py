# 2019/08/05

input=open(0).readline

n,m=map(int,input().split())
edge=[[] for _ in range(n)]
for i in range(m):
    a,b=map(int,input().split())
    a-=1;b-=1
    edge[a].append(b)
    edge[b].append(a)


for e in edge[-1]:
    if 0 in edge[e]:
        print('POSSIBLE')
        exit()

print('IMPOSSIBLE')
