# yukicoder No.111 あばばばば 2020/03/01

l=int(input())
b=l//2
a=l-b

ans=(a**2-a)//2 + (b**2-b)//2
print(ans)