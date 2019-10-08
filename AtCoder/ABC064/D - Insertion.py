# 2019/09/20
from collections import deque

n=int(input())
s=list(input())

l=s.count('(')
r=s.count(')')

cnt=0
cntL=0

def solve(w,r,s):
    cnt=0
    res=0
    for i in range(n):
        if s[i]==w:
            if cnt:
                cnt-=1
            else:res+=1
        else:
            cnt+=1    
    return list(r*res)




pre=solve(')','(',s)
suf=solve('(',')',s[::-1])
ans=pre+s+suf
print(''.join(ans))