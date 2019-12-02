# 2019/12/1

n=int(input())
s=list(input())

fst=[]
tmp=set()
for i in range(n):
    tmp.add(s[i])
    fst.append(list(tmp))

trd=[]
tmp=set()
for i in range(n):
    tmp.add(s[n-1-i])
    trd.append(list(tmp))
trd=trd[::-1]
cnt=set()
for i in range(1,n-1):
    for f in fst[i-1]:
        for t in trd[i+1]:
            cnt.add(f+s[i]+t)
print(len(cnt))