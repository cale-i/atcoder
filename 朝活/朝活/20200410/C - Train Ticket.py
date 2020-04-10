# https://atcoder.jp/contests/abc079/tasks/abc079_c

a,b,c,d=list(input())
op=['+','-']

def calc():
    for op1 in op:
        for op2 in op:
            for op3 in op:
                res=a+op1+b+op2+c+op3+d
                if eval(res)==7:
                    return res

print(calc()+'=7')