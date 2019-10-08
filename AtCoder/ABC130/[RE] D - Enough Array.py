# 2019/06/30
# 考え方
# Lを固定したとき､部分和が条件を満たす最小のRを探す
# 最小のR以降を加算しても条件を満たし続けるため､全体(n)-最小のR(r)+1を加算し､Lを増加させる


n,k=map(int,input().split())
a=list(map(int,input().split()))

r=0
res=0
cnt=0

for l in range(n):
    
    while r<n and cnt<k:
        cnt+=a[r]
        r+=1

    if cnt>=k:res+=n-r+1 # <= 思いつかなかった
    
    if r==l:r+=1
    else:cnt-=a[l]

print(res)


# 2019/06/30
# 累積和で解いてみる

from itertools import accumulate

n,k=map(int,input().split())
a=[0]+list(accumulate(map(int,input().split())))

res=0
r=0
for l in range(n):
    while r<n and a[r]-a[l]<k:
        r+=1

    if a[r]-a[l]>=k:res+=n-r+1
    if r==l:r+=1
    
print(res)