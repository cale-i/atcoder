# yukicoder No.842 初詣 2020/01/21

*coins,g=map(int,input().split())

values=[500,100,50,10,5,1]

ans='YES'
for c,v in zip(coins,values):
    if c==0:continue
    if g>=v:
        g-=v*(min(c,g//v))
    if g==0:break
else:
    ans='NO'
print(ans)