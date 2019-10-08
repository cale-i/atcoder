# 2019/08/09

n=int(input())
a=list(map(int,input().split()))

sec=0
quad=0
rem=0
for i in range(n):
    if a[i]%4==0:
        quad+=1
    elif a[i]%2==0:
        sec+=1
    else:
        rem+=1

if sec>0:rem+=1
if rem-quad<=1:
    print('Yes')
else:print('No')