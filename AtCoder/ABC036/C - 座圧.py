# 2019/08/18

input=open(0).readline

n=int(input())
a=[int(input()) for _ in range(n)]

sa=sorted(a)

pre=-1
cnt=0
ans={}
for i in range(n):
    if pre==sa[i]:continue
    ans[sa[i]]=cnt
    pre=sa[i]
    cnt+=1
for i in range(n):
    print(ans[a[i]])