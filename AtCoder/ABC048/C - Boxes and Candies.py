# 2019/08/16

n,x=map(int,input().split())
a=list(map(int,input().split()))


def solve():
    cnt=0
    for i in range(n-1):
        tmp=a[i]+a[i+1]-x
        if tmp>0:
            cnt+=tmp
            if tmp>a[i+1]:
                buf=tmp-a[i+1]
                a[i]-=buf
                tmp-=buf
            a[i+1]-=tmp
    return cnt

ans=solve()
print(ans)