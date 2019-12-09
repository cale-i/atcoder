# 2019/12/09

n=int(input())
xy=[]
for i in range(n):
    a=int(input())
    lst=[1]*n
    for j in range(a):
        x,y=map(int,input().split())
        x-=1
        lst[x]=y
    xy.append(lst)

ans=0
for bit in range(1,2**n):
    ret=[1]*n
    for idx in range(n):
        if bit&(1<<idx):
            ret=list(map(lambda x,y:(x&y),xy[idx],ret))
    BIT=bin(bit).count('1')
    RET=''.join(map(str,ret)).count('1')
    if BIT==RET:
        ans=max(ans,BIT)

print(ans)