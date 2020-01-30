# yukicoder No.378 名声値を稼ごう 2020/01/31

n=int(input())
res=n
mx=n*2
while n:
    n//=2
    mx=max(mx,res+n*2)
    res+=n
print(mx-res)