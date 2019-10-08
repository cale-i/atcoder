# 2019/07/30
# だめだめ

n=int(input())
a=list(map(int,input().split()))

if n==1:
    print(0)
    exit()

res=0
i=1
s=0
for i in range(1,n):
    if a[i-1]==a[i]:continue

    sign=1 if a[i-1]<a[i] else -1

    if sign==s:
        continue
    else:
        res+=1
        s=sign

if s==0:
    print(0)
else:
    print(res+1)