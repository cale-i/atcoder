# 2019/08/06
# 式変形で手こずった

N=int(input())

def solve(N,h,n):
    
    if (4*h*n-(N*n)-(N*h)) and (N*h*n)%(4*h*n-(N*n)-(N*h))==0:
        return (N*h*n)//(4*h*n-(N*n)-(N*h))
    else: return 0
lim=3500
for h in range(1,lim+1):
    if 1/h>=4/N:continue
    for n in range(1,lim+1):
        w=solve(N,h,n)
        if w>0:
            print(h,n,w)
            exit()