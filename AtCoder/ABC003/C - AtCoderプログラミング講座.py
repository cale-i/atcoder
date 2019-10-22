# 2019/10/22

n,m=map(int,input().split())
r=sorted(list(map(int,input().split())),reverse=True)[:m]

cnt=0
while r:
    cnt+=r.pop()
    cnt/=2
print(cnt)