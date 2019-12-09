# 2019/11/30

# だめ
全国統一プログラミング王決定戦予選
from bisect import bisect_left

n,m=map(int,input().split())
s=list(input())[::-1]

mz=[i for i,e in enumerate(s) if e=='0']
ans=[]

def nbtn(key):
    idx=bisect_left(mz,key)
    if idx>=len(mz):return mz[-1]
    if mz[idx]==key:
        res=mz[idx]
    else:
        res=mz[idx-1]
    return res


i=0
key=m
while i<=len(mz):
    key=nbtn(key)
    res=key-i
    if res==0:
        if i+1==len(mz):break
        else:
            print(-1)
            exit()
    ans.append(res)
    i=key
    key+=m
print(*ans[::-1],sep=' ')