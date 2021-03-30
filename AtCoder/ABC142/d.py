# 2019/09/28
from fractions import gcd

a,b=map(int,input().split())


# 約数列挙

def divisors(n):
    div=[]
    if n%2==0:div.append(2)
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            if i%2:
                div.append(i)
                if i!=n//i and n//i%2:
                    div.append(n//i)
    # div.sort()
    return div

diva=divisors(a)
divb=divisors(b)
div=set()
for aa,bb in zip(diva,divb):
    if aa in divb:
        div.add(aa)
    if bb in diva:
        div.add(bb)

cnt=1
res=[]

res=[]
for i in div:
    if i==1:continue
    for j in div:
        if j==1:continue
        if i==j:continue
        if i in res and j in res:continue
        if gcd(i,j)==1:
            continue
        else:
            break
    else:
        cnt+=1
        res.append(i)
print(cnt)