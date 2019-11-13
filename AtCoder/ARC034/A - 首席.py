# 2019/11/13

n=int(input())
ans=-1
for i in range(n):
    *abcd,e=map(int,input().split())
    ans=max(ans,sum(abcd)+e*110/900)
print(ans)