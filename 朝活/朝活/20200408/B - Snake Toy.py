# https://atcoder.jp/contests/abc067/tasks/abc067_b

n,k=map(int,input().split())
l=sorted(map(int,input().split()),reverse = True)
ans=sum(l[:k])
print(ans)