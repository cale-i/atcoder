# 2019/09/21

n=int(input())
a=list(map(int,input().split()))

cnt=1
for e in a:
    if e%2:
        cnt*=1
    else:
        cnt*=2
print(3**n-cnt)
        