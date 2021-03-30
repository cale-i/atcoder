# 2020/01/06
# 差集合とるだけ

n=int(input())
aa=[]
bb=[]
for i in range(n):
    a,b=input().split()
    aa.append(a)
    bb.append(b)

res=set(bb)-set(aa)

for b in bb:
    if b in res:
        print(b)
        res.remove(b)