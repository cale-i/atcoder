# 2019/08/07

a,b,c,d,e,f=map(int,input().split())

max_a=f//100*a
max_b=f//100*b
min_ab=min(a,b)*100
max_c=(f-min_ab)//c
max_d=(f-min_ab)//d


def solve():
    cnt=0   
    ans=0   
    for i in range(max_a):
        if i*a>f:break
        for j in range(max_b):
            if i==j==0:continue
            if (i*a+j*b)*100>f:break

            for k in range(max_c):
                if (i*a+j*b)*100+k*c>f:break
                for l in range(max_d):
                    if k==l==0:continue
                    if (i*a+j*b)*100+k*c+l*d>f:break
                    w=(i*a+j*b)*100
                    s=k*c+l*d
                    D=s/w
                    if D>e/100:break
                    if cnt<D:
                        ans=(w+s,s)
                        cnt=D
                    if D==e/100:
                        return ans
    return ans
ans=solve()
if ans==0:
    print(min(a,b)*100,0)
else:print(*ans)