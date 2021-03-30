# 2019/08/17
# だめ


n,a=map(int,input().split())
x=list(map(int,input().split()))

sumx=sum(x)
num=[i*a for i in range(1,n+1)]
dp=[[0]*(sumx+1) for _ in range(n+1)]
dp[0][0]=1

for i in range(n):
    for j in range(sumx):
        if j-x[i]>=0:
            dp[i+1][j]=dp[i][j]+dp[i][j-x[i]]
        else:
            dp[i+1][j]=dp[i][j]

ans=0
for i in num:
    if i>len(dp[-1]):break
    ans+=dp[-1][i]
print(ans)