# 2019/11/5

n=int(input())
r,b=0,0
for i in range(n):
    s=input()
    r+=s.count('R')
    b+=s.count('B')
res=r-b
if res:
    if res>0:print('TAKAHASHI')
    else:print('AOKI')
else:
    print('DRAW')