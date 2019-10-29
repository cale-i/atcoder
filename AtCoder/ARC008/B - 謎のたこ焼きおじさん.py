# 2019/10/29

from collections import Counter
input()
name=Counter(input())
kit=Counter(input())
ans=0
for k,v in name.items():
    if k in kit:
        ans=max(ans,-(-v//kit[k]))
    else:
        ans=-1
        break
print(ans)