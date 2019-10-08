# 2019/09/09

n,k=map(int,input().split())
t=set(map(int,input().split()))

def solve(t):
    tt=set(map(int,input().split()))
    ret=set()
    for a in t:
        for b in tt:
            ret.add(a^b)
    return ret
for i in range(n-1):
    t=solve(t)

if 0 in t:
    print('Found')
else:
    print('Nothing')