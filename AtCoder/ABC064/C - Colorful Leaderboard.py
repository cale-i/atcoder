# 2019/08/08

from bisect import bisect_left

n=int(input())
a=sorted(list(map(int,input().split())))

pre=0
cnt=0
for i in range(1,9):
    idx=bisect_left(a,i*400)
    if idx==pre or idx==0:continue
    cnt+=1
    pre=idx

    
if idx<n:
    if cnt==0:
        cnt+=1
        res=n-idx
    else:
        res=n-idx+cnt

else:res=cnt
print(cnt,res,sep=' ')