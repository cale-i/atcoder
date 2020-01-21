# yukicoder No.846 メダル 2020/01/21

p,q,r=map(int,input().split())
a,b,c=map(int,input().split())


min_n=max((a-1)*p,(a+b-1)*q,(a+b+c-1)*r)+1
max_n=min(a*p,(a+b)*q,(a+b+c)*r)
if min_n>max_n:
    print(-1)
else:
    print(*[min_n,max_n])