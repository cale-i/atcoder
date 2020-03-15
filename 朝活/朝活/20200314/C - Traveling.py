import sys
input=sys.stdin.readline

n=int(input())

pt=0
pxy=0
for i in range(n):
    t,x,y=map(int,input().split())
    dt=t-pt
    dxy=abs(x+y-pxy)
    if dxy>dt or dt%2!=dxy%2:
        print('No')
        exit()
else:
    print('Yes')