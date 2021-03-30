# yukicoder No.441 和か積 2020/01/30

a,b=map(int,input().split())
add_ab=a+b
mul_ab=a*b
if add_ab==mul_ab:
    print('E')
else:
    print('S' if add_ab>mul_ab else 'P')