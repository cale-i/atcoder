# yukicoder No.745 letinopia raoha 2020/01/22

a,b,c,d=map(int,input().split())
if d==10:
    print('Impossible')
    exit()
print('Possible')
ml=0
score=0
tmp=0
while b:
    tmp=min(100,b)
    score+=tmp*50*(2**(ml//100))
    ml+=tmp
    b-=tmp

tmp2=min(100-(tmp%100),a)
score+=tmp2*100*(2**(ml//100))
ml+=tmp2
a-=tmp2

while a:
    tmp=min(100,a)
    score+=tmp*100*(2**(ml//100))
    ml+=tmp
    a-=tmp
print(score)