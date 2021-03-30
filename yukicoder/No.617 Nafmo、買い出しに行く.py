# yukicoder No.617 Nafmo、買い出しに行く 2020/01/26
# DP

n,k=map(int,input().split())
a=[int(input()) for _ in range(n)]

dp=[0]*(k+1)
dp[0]=1
for i in range(n):
    for j in reversed(range(k+1)):
        if j<a[i]:continue
        if dp[j-a[i]]:
            dp[j]=1
for i in reversed(range(0,k+1)):
    if dp[i]:
        print(i)
        exit()
else:
    print(0)