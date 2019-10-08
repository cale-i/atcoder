# 2019/09/25

m,n,N=map(int,input().split())
cnt=N
while N>=m:
    s=(N//m)*n
    cnt+=s
    N=s+N%m
print(cnt)