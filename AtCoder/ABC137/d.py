# 2019/08/10

import sys

input=sys.stdin.readline

n,m=map(int,input().split())
s=[]
for i in range(n):
    a,b=map(int,input().split())
    s.append((a,b))

s=sorted(s,key=lambda x:(x[0],-x[1]))
res=-1

dp=[0]*(m+1)
pre=s[0][0]
i=0

for k,v in s:
    j=0
    if k==pre:
        i+=1
    else:i=k
    if k>m:break
    if dp[i]<v:dp[i]=v
    else:
        while j+i<m  and dp[i+j]>=v:
            j+=1
        if dp[i+j]<v:
            dp[i+j]=v
    
print(sum(dp))