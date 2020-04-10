# https://atcoder.jp/contests/abc139/tasks/abc139_b

a,b=map(int,input().split())
ans=-(-(b-a)//(a-1))
print(ans+1)