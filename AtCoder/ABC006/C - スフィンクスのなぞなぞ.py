# 2019/07/15

n,m=map(int,input().split())

if m%2==0:B=list(range(0,n+1,2))
else:B=list(range(1,n+1,2))

for b in B:
    if (m-3*b)%2!=0:continue
    c=(m-3*b)//2+b-n
    a=n-(b+c)
    if a<0 or b<0 or c<0:continue
    if a+b+c==n:
        print('{} {} {}'.format(a,b,c))
        break
else:
    print('-1 -1 -1')
