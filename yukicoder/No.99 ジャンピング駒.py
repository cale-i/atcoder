# yukicoder No.99 ジャンピング駒 2020/03/01

n=int(input())
x=list(map(int,input().split()))
odd,even=0,0

for e in x:
    if e%2:odd+=1
    else:even+=1

print(abs(odd-even))