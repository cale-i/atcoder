# 2019/08/31

from collections import Counter

input()
r=Counter(input())

ans=0
cnt=0
for k,v in r.items():
    if k=='A':
        ans+=v*4
    if k=='B':
        ans+=v*3
    if k=='C':
        ans+=v*2
    if k=='D':
        ans+=v*1
    cnt+=v
print(ans/cnt)



# 改良

from collections import Counter

n=int(input())
r=Counter(input())
ans=0
for ml,e in enumerate('DCBA',1):
    ans+=r[e]*ml
print(ans/n)