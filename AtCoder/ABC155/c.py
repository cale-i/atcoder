from collections import Counter

n=int(input())
s=[input() for _ in range(n)]
c=Counter(s)
mx=c.most_common()[0][1]
ans=[]
for e in c.most_common():
    if mx==e[1]:
        ans.append(e[0])
ans.sort()
print(*ans,sep='\n')