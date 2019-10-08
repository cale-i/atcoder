# 2019/08/15

n=int(input())
s=input()
t=input()

def solve():
    for i in range(n):
        for j in range(n):
            if s[i]!=t[j]:continue
            m=s[i:]
            if m==t[:len(m)]:
                res=len(s[:i])+n
                return res
ans=solve()
if ans:print(ans)
else:print(2*n)