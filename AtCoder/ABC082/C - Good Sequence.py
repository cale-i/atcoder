# 2018/08/05
from collections import Counter

n=int(input())
a=Counter(list(map(int,input().split())))

cnt=0
for k,v in a.items():
    if k<v:
        cnt+=v-k
    elif k>v:
        cnt+=v
print(cnt)