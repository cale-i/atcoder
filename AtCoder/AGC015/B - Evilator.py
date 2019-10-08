# 2019/09/04

s=list(input())
n=len(s)

cnt=0
for i in range(n):
    if s[i]=='U':
        cnt+=n-i-1
        cnt+=i*2
    else:
        cnt+=(n-i-1)*2
        cnt+=i
print(cnt)