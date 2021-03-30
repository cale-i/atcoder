# 2019/09/25
"""
n,m,l=map(int,input().split())
p,q,r=map(int,input().split())

ans=0
def solve(a,b,c):
    return (n//a)*(m//b)*(l//c)

ans=max(ans,
        solve(p,q,r),
        solve(p,r,q),
        solve(q,p,r),
        solve(q,r,p),
        solve(r,p,q),
        solve(r,q,p))
print(ans)"""

# ぱーみゅてーしょんver

from itertools import permutations

n,m,l=map(int,input().split())
P=map(int,input().split())

ans=0
def solve(a,b,c):
    return (n//a)*(m//b)*(l//c)
for p,q,r in permutations(P):
    ans=max(ans,solve(p,q,r))
print(ans)