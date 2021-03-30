# 2019/11/25

from collections import Counter

n=int(input())
s=[''.join(sorted(input())) for _ in range(n)]
c=Counter(s)
ans=0
for k,v in c.items():
    ans+=(v*(v-1))//2
print(ans)