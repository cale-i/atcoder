# yukicoder No.149 碁石の移動 2020/02/07

aw,ab=map(int,input().split())
bw,bb=map(int,input().split())
c,d=map(int,input().split())

mb=min(c,ab)
mw=c-mb
bw+=mw
bb+=mb
aw-=mw
mw=min(d,bw)
ans=mw+aw
print(ans)