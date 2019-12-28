# 2019/12/28
# DP

n=int(input())
v=[0]+list(map(int,input().split()))
dp=[0]*(n+1)
dp[0]=v[0]
dp[1]=v[1]

for i in range(2,n+1):
    dp[i]=max(dp[i-2]+v[i],dp[i-1])
print(dp[-1])