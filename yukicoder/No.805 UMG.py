# yukicoder No.805 UMG 2020/01/22

n=int(input())
s=input()

U,M,G=set(),set(),set()
for i,e in enumerate(s,1):
    if e=='U':
        U.add(i)
    elif e=='M':
        M.add(i)
    else:
        G.add(i)
else:
    if not(U and M and G):
        print(0)
        exit()
cnt=0
for u in U:
    for m in M:
        if u>m:continue
        g=m+m-u
        if not(u<m<g):continue
        if m+m-u in G:
            cnt+=1
print(cnt)