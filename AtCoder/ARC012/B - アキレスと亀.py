# 2019/11/8

n,va,vb,l=map(int,input().split())

def solve(n,l):
    if n:solve(n-1,l*vb/va)
    else:print(l)
solve(n,l)