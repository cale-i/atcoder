# 2019/11/16

n=int(input())
s=list(input())

if n%2==0:
    if s[:n//2]==s[n//2:]:
        print('Yes')
        exit()
print('No')