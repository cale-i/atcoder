# 2019/11/11

n=int(input())
tbl='aeiouy,.'
del_table={}
for e in tbl:
    del_table[e]=''

del_table=str.maketrans(del_table)

cnv_table={}
for i,v in enumerate('bcdwtjfqlvsxpmhkngzr',1):
    if i%2:idx=i//2+1
    else:idx=i//2
    idx%=10
    cnv_table[v]=str(idx)
cnv_table=str.maketrans(cnv_table)

w=list(map(lambda x:x.lower(),input().split()))

ans=[]
for e in w:
    tmp=e.translate(del_table)
    res=tmp.translate(cnv_table)
    if res:
        ans.append(res)
print(*ans)