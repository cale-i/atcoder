# yukicoder No.526 フィボナッチ数列の第N項をMで割った余りを求める 2020/01/28

n,m=map(int,input().split())

fib=[0,1]
for i in range(n-2):
    fib[1],fib[0]=(fib[0]+fib[1])%m,(fib[1])%m
print(fib[1]%m)