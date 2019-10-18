# 2019/09/23

from collections import Counter
n=int(input())
d=Counter(list(map(int,input().split())))
m=int(input())
t=Counter(list(map(int,input().split())))

for k,v in t.items():
    d[k]=d.get(k,0)-v
    if d[k]<0:
        print('NO')
        exit()
print('YES')