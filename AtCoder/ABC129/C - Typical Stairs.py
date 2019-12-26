# 2019/12/26

mod=10**9+7
n,m=map(int,input().split())
a=[int(input()) for _ in range(m)]
dp=[0]*(n+1)
dp[0]=1
dp[1]=1
for aa in a:
    dp[aa]=-1

for i in range(2,n+1):
    if dp[i]==-1:continue
    if dp[i-1]!=-1:
        dp[i]+=dp[i-1]
    if dp[i-2]!=-1:
        dp[i]+=dp[i-2]
print(dp[-1]%mod)