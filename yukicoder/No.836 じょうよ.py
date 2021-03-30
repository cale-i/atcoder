# yukicoder No.836 じょうよ 2020/01/21

from collections import Counter

l,r,n=map(int,input().split())

res=[]
dic={}
for i in range(l,min(l+n,r+1)):
    num=i%n
    res.append(num)
    dic[num]=dic.get(num,0)+1
d,m=divmod((r-l+1),n)

dic={k:v*d for k,v in dic.items()}

C=Counter(dic)
C.update(res[:m])

[print(C[i])for i in range(n)]