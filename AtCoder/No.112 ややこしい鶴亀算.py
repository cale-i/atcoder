# yukicoder No.112 ややこしい鶴亀算 2020/02/13

n=int(input())
a=list(map(int,input().split()))

ct=sum(a)//(n-1)
c,t=0,0
for e in a:
    if ct-e==2:
        c+=1
    else:
        t+=1
print(*[c,t])