# 2019/09/05

a,b=map(int,input().split())

cnt=0
while a!=b:
    if a>b:a,b=b,a
    x=abs(a+10-b)
    y=abs(a+5-b)
    z=abs(a+1-b)
    if min(x,y,z)==x:a+=10
    elif y<z:a+=5
    else:a+=1     
    cnt+=1

print(cnt)
