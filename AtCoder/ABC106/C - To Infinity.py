# 2019/07/13

s=list(map(int,list(input())))
k=int(input())

if len(s)>=k and sum(s[:k-1])==k-1:
    ans=s[k-1]
else:
    for e in s:
        if e!=1:
            ans=e
            break

print(ans)