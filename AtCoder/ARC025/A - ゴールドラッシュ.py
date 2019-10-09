# 2019/10/09

d=map(int,input().split())
j=map(int,input().split())

cnt=0
for dd,jj in zip(d,j):
    cnt+=max(dd,jj)
print(cnt)