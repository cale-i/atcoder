# 2019/10/17

R,G,B,n=map(int,input().split())
cnt=0
for i in range(n//R+1):
    r=i*R
    for j in range((n-r)//G+1):
        g=j*G
        b=n-(r+g)
        if b%B:continue
        cnt+=1
print(cnt)