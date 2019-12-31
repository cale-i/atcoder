# 2019/12/30

import math

n1,d1=map(int,input().split())
p=input()
n2,d2=map(int,input().split())
ans1=0
ans2=0
if p in ['+','-']:
    ans1=eval(f'{n1}*{d2}{p}{n2}*{d1}')
    ans2=d1*d2
else:
    if p=='/':
        p='*'
        n2,d2=d2,n2
    ans1=n1*n2
    ans2=d1*d2
gcd=math.gcd(ans1,ans2)
ans1//=gcd
ans2//=gcd
if ans2==1:
    print(ans1)
else:
    print(ans1,ans2,sep=' ')