# 2019/12/29

n=int(input())
w=list(map(int,input().split()))
w_sum=sum(w)
half=w_sum//2

if half*2!=w_sum:
    print('impossible')
    exit()

dp=[0]*(w_sum+1)
dp[0]=1

for i in range(len(w)):
    for j in reversed(range(w[i],w_sum+1)):
        if dp[j-w[i]]:
            dp[j]=1
    if dp[half]:break

if dp[half]:print('possible')
else:print('impossible')