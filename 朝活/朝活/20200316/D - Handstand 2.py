# https://atcoder.jp/contests/abc152/tasks/abc152_d
# 解説かんにんぐ

n=int(input())
freq=dict()
ans=0

for i in range(1,n+1):
    s=str(i)
    p=(s[0],s[-1])
    freq[p]=freq.get(p,0)+1

for i in range(1,n+1):
    s=str(i)
    q=(s[-1],s[0])
    ans+=freq.get(q,0)
print(ans)