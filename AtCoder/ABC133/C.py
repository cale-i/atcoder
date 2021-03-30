l,r=map(int,input().split())

if r//673-l//673>0 and r//3-l//3>0:
    print(0)


else:
    res=float('inf')
    for i in range(l,l+2019):
        ed=min(r-l+2019,2019+i)
        for j in range(i+1,ed):
            res=min((i*j)%2019,res)
    print(res)
