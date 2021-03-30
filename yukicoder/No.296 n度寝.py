# 2019/12/28

n,h,m,t=map(int,input().split())
hh,M=divmod(m+((n-1)*t),60)
H=(hh+h)%24
print(H,M,sep=('\n'))