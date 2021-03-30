# 2019/07/19

n,x=map(int,input().split())
s=input()
cnt=0
for i in range(n):
    t=int(input())
    if s[i]=='0':cnt+=t
    else:cnt+=min(t,x)
print(cnt)
    