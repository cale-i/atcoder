# 2019/07/24

from collections import Counter

n=int(input())
v=list(map(int,input().split()))

even=[]
odd=[]

for i in range(n):
    if i%2==0:even.append(v[i])
    else:odd.append(v[i])

e=Counter(even).most_common(2)
if len(e)<2:e=[e[0][0]]
else:e=list([e[0][0]]+[e[1][0]])
o=Counter(odd).most_common(2)
if len(o)<2:o=[o[0][0]]
else:o=list([o[0][0]]+[o[1][0]])

ans=float('inf')
for i in e:
    for j in o:
        cnt=0
        if i==j:continue
        for k in range(n):
            if k%2==0 and v[k]!=i:
                cnt+=1
            elif k%2==1 and v[k]!=j:
                cnt+=1
        ans=min(cnt,ans)

if ans==float('inf'):ans=n//2
print(ans)