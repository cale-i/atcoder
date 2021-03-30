# 2019/10/08

from collections import Counter
map(int,input().split())
L=Counter(map(int,input().split()))
R=Counter(map(int,input().split()))
cnt=0

for lk,lv in L.items():
    if R[lk]>0:
        cnt+=min(L[lk],R[lk])
print(cnt)