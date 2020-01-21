# yukicoder No.825 賢いお買い物 2020/01/21

a,b,c=map(int,input().split())
if a+b<c and b<1:
    print('Impossible')
    exit()
else:
    rm=(a+b)-c
    if rm<0:
        n=10-(-rm+1)
        ans=n
    else:
        aa=min(a,rm)
        bb=10*(max(0,rm-a))
        if a>aa>=10:
            aa-=10-1
        ans=aa+bb
if ans<1:
    print('Impossible')
else:print(ans)