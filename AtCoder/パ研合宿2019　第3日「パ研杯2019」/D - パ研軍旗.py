# 2019/12/27

M=5
n=int(input())
dp_r=[0]*(n+1)
dp_b=[0]*(n+1)
dp_w=[0]*(n+1)

s=[list(input()) for _ in range(5)]

r,b,w=[[M]*(n+1) for _ in range(3)]

for i in range(5):
    for j in range(n):
        if s[i][j]=='R':r[j]-=1
        elif s[i][j]=='B':b[j]-=1
        elif s[i][j]=='W':w[j]-=1

for i in range(1,n+1):
    dp_r[i]=min(dp_b[i-1],dp_w[i-1])+(r[i-1])
    dp_b[i]=min(dp_r[i-1],dp_w[i-1])+(b[i-1])
    dp_w[i]=min(dp_r[i-1],dp_b[i-1])+(w[i-1])

print(min(dp_r[-1],dp_b[-1],dp_w[-1]))