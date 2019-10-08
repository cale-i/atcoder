# 2019/08/29

n,a=map(int,input().split())
n//=3
if a==0:
    print('0 0')
    exit()
ans=[-(-a//3),min(a,n)]
print(*ans)