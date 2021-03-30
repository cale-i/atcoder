# 2019/09/08
# ようつべ解説観て

n,k=map(int,input().split())
s=list(input())

cnt=0
res=0
for i in range(n-1):
    if s[i]==s[i+1]:
        res+=1
    else:
        cnt+=1
res+=min(cnt,k)*2
res=min(n-1,res)

print(res)
