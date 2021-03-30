# https://atcoder.jp/contests/abc089/tasks/abc089_c

from itertools import combinations

n=int(input())
s=[input() for _ in range(n)]

S=dict()
w=['M','A','R','C','H']

for e in s:
    fst=e[0]
    if fst in w:
        S[fst]=S.get(fst,0)+1

C=list(combinations(S,3))

ans=0
for c in C:
    tmp=1
    for e in c:
        tmp*=S[e]
    ans+=tmp
print(ans)