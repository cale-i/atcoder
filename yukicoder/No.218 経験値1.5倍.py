# yukicoder No.218 経験値1.5倍 2020/02/03

a=int(input())
b=int(input())
c=int(input())

ab=-(-a//b)
ac=-(-a//c)
print('YES' if (ac/ab)<=2/3 else 'NO')