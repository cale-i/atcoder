# 2019/07/18

n,d=map(int,input().split())
s=[list(map(int,input().replace('o','1').replace('x','0'))) for _ in range(d)]

ans=0
for i in range(d):
    for j in range(i+1,d):
        res=[s[i][k]|s[j][k] for k in range(n)]
        ans=max(ans,sum(res))
print(ans)