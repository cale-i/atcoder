# 2019/08/08

from collections import Counter

input()
a=Counter(list(map(int,input().split())))

x=sorted(list(a.items()),reverse=True)



ans=0
for k,v in x:
    if v<2:continue
    if v>3:
        if ans==0:
            ans=k**2
        else:
            ans*=k
        break
    else:
        if ans==0:
            ans=k
        else:
            ans*=k
            break

print(ans)