# 2019/08/15

a,b=map(int,input().split())
if a>0:ans=('Positive')
elif b<0:
    if -(a+b-1)%2:
        ans=('Negative')
    else:
        ans=('Positive')
else:ans=('Zero')

print(ans)