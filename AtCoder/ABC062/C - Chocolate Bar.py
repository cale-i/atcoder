# 2019/09/03

h,w=map(int,input().split())

if (h*w)%3==0:
    print(0)
    exit()


def solve(s):
    global h,w
    
    cnt=float('inf')
    if s==h:
        H,W=w,h
    else:
        H,W=h,w
    for i in range(1,s+1):
        a=i*H
        rest=H*(w-i)
        if rest%2==0:
            b=c=rest//2
        else:
            ww=W-i
            hh=H
            bb=max(ww,hh)//2
            cc=bb+1
            b=min(ww,hh)*bb
            c=min(ww,hh)*cc
        cnt=min((max(a,b,c)-min(a,b,c)),cnt)

    return cnt


ans=min(solve(h),solve(w))
print(ans)
        
