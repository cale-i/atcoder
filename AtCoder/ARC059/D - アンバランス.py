# 2019/09/11

s=list(input())
n=len(s)

if n<3:
    print(*[1,2] if len(set(s))<2 else [-1,-1])

    exit()

ans=(-1,-1)
for i in range(1,n-1):
    if len(set(s[i]+s[i-1]+s[i+1]))<3:
        ans=(i,i+2)
        break
print(*ans)