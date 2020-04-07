# https://atcoder.jp/contests/agc021/tasks/agc021_a

s=list(input())
sm=sum(map(int,s))
n=len(s)
res=int(s[0])-1+9*(n-1)
print(max(res,sm))