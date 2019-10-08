# 2019/07/25

input=open(0).readline

n,k=map(int,input().split())
h=[int(input()) for _ in range(n)]

h.sort()
ans=float('inf')
for i in range(n-(k-1)):
    res=h[i+k-1]-h[i]
    ans=min(ans,res)

print(ans)