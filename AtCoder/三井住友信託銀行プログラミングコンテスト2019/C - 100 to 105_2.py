# 2019/12/7

# DPver

x=int(input())

dp=[0]*(x+1)
c=[100,
   101,
   102,
   103,
   104,
   105]

dp[0]=1
for i in range(len(c)):
    for j in range(1,x+1):
        if c[i]>j:continue
        if dp[j-c[i]]:dp[j]=1
print(1 if dp[-1] else 0)