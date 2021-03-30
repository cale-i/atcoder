# 2019/08/24
#DFS

n=int(input())
edge=[[] for _ in range(n)]

for i in range(1,n):
    x=int(input())
    x-=1
    edge[x].append(i)

def dfs(p):
    if len(edge[p])<1:
        return 1
    
    tmp=[]
    for e in edge[p]:
        tmp.append(dfs(e))
    if len(tmp)<2:
        cnt=(int(*tmp)*2+1)
        return cnt
    cnt=max(tmp)+min(tmp)+1
    return cnt

ans=dfs(0)
print(ans)