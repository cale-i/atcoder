# 2019/12/14

from collections import Counter

s=input()
st=set(s)
n=len(s)//len(st)
c=Counter(s)

for v in c.values():
    if v!=n:
        print('No')
        exit()
else:print('Yes')