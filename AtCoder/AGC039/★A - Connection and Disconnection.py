# 2019/10/07

s=list(input())
n=len(s)
k=int(input())
cnt=0
if n==1:
    print(k//2)
    exit()
s*=2
nn=n*2
i,j=0,0
cnt=0
for i in range(1,nn):
    if s[i]==s[i-1]:
        cnt+-1
cnt*=2
if s[0]==s[-1]:
    cnt-=1


print(cnt*k)



