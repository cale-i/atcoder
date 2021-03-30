# 2019/11/24
import sys
sys.setrecursionlimit(10**9)

n=int(input())
ab=[]
edge=[[] for _ in range(n)]
for i in range(n-1):
    a,b=map(int,input().split())
    a,b=a-1,b-1
    ab.append((a,b))
    edge[a].append(b)

ans={}
def solve(p,c):
    global ans
    cnt=1
    for vtx in edge[p]:
        while c==cnt:
            cnt+=1
        ans[(p,vtx)]=cnt
        solve(vtx,cnt)
        cnt+=1

solve(0,0)
print(max(ans.values()))
for e in ab:
    print(ans[e])
