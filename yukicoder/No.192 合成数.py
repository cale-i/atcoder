# yukicoder No.192 合成数 2020/02/03

n=int(input())
n-=100
if n<4:
    print(4)
else:
    print(n+1 if n%2 else n)