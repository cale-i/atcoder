# 2019/11/10

b=list(map(str,input().split()))
d=list(map(str,range(10)))
t={}
r={}
for bb,dd in zip(b,d):
    t[bb]=dd
    r[dd]=bb
tbl=str.maketrans(t)
rev_tbl=str.maketrans(r)
ans=[]
for i in range(int(input())):
    ans.append(int(input().translate(tbl)))
ans.sort()
for e in map(str,ans):
    print(e.translate(rev_tbl))