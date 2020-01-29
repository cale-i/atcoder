# yukicoder No.436 ccw 2020/01/30

s=list(input())
n=len(s)
for i in range(n-1):
    if s[i]+s[i+1]=='cw':
        ans=min(n-(i+1),i)
print(ans)