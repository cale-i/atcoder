# 2019/09/12

n=int(input())
C=input()

a=C.count('1')
b=C.count('2')
c=C.count('3')
d=C.count('4')

print(max(a,b,c,d),min(a,b,c,d))