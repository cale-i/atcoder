# 2019/07/15
# DP
# 動的計画法 (1次元)

n=int(input())
a=list(map(int,input().split()))
dp=[float('inf')]*n
dp[0]=0

for i in range(0,n-1):
    dp[i+1]=min(dp[i+1],dp[i]+abs(a[i]-a[i+1]))
    if i+2<n:dp[i+2]=min(dp[i+2],dp[i]+abs(a[i]-a[i+2]))
print(dp[-1])

