# yukicoder No.858 わり算 2020/01/20

a,b=map(int,input().split())
d,r=divmod(a,b)
a=r
ans=[str(d),'.']

for i in range(50):
    d,r=divmod(a,b)
    if d==0:
        a*=10
        d,r=divmod(a,b)
    ans.append(str(d))
    a=r

print(''.join(ans))


# 別解2(先に10**50かけちゃう)

a,b=map(int,input().split())
d,r=divmod(a,b)
imag=r*10**50//b

print(f'{d}.{imag:0=50}')