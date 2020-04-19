# https://atcoder.jp/contests/arc013/tasks/arc013_1

n,m,l=map(int,input().split())
pqr=list(map(int,input().split()))

def solve(w,d,h):
    return (n//w) * (m//d) * (l//h)

ans=0
for i in range(3):
    for j in range(3):
        if i==j:continue
        for k in range(3):
            if i==k or j==k:continue
            ans=max(ans,solve(pqr[i],pqr[j],pqr[k]))

print(ans)