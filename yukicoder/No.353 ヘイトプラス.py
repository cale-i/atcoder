# yukicoder No.353 ヘイトプラス 2020/02/01

a,b=map(int,input().split())
a=bin(a)[2:]
b=bin(b)[2:]
n=max(len(a),len(b))
a=a.zfill(n)
b=b.zfill(n)
a=a[::-1]
b=b[::-1]
res=[]

c=0
for x,y in zip(a,b):
    x,y=int(x),int(y)
    res.append(x^y^c)
    c=1 if [x,y,c].count(1)>1 else 0
else:
    res.append(c)
res=res[::-1]
ans=int(''.join(map(str,res)),2)
print(ans)