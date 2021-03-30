# 2019/08/25

s=input()
k=int(input())

n=len(s)
k%=n

ans=s[k:]+s[:k]
print(ans)