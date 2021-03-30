# 2019/12/22

n=int(input())
s,t=input().split()
ans=[]
for i in range(n):
    ans.append(s[i]+t[i])
print(*ans,sep='')