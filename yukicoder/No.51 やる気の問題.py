# yukicoder No.51 やる気の問題 2020/03/08

w=int(input())
d=int(input())

while w:
    tmp=w//(d**2)
    w-=tmp
    d-=1
print(tmp)