# 2019/11/25

N,T=map(int,input().split())
ans=float('inf')
for i in range(N):
    c,t=map(int,input().split())
    if T<t:continue
    ans=min(ans,c)
if ans==float('inf'):
    ans='TLE'
print(ans)