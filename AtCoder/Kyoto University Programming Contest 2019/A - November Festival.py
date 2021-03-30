# 2019/10/16

n,x=map(int,input().split())
a=list(map(int,input().split()))

max_a=max(a)
cnt=0
for e in a:
    if e+x>=max_a:
        cnt+=1

print(cnt)