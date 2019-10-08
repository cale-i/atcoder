# 2019/09/30

n,l=map(int,input().split())
s=list(input())

cnt=1
res=0
for e in s:
    if e=='+':
        cnt+=1
    else:
        if cnt>1:
            cnt-=1
    if cnt>l:
        cnt=1
        res+=1
print(res)