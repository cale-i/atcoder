# yukicoder No.432 占い(Easy) 2020/01/30

from scipy.special import comb

t=int(input())
s=[list(map(int,list(input()))) for _ in range(t)]

for e in s:
    n=len(e)
    res=0
    if n==1:
        print(*e)
    elif n==2:
        res=sum(e)
        if res%9:
            print(res%9)
        else:
            if res==0:
                print(0)
            else:
                print(9)
    else:
        for k,f in enumerate(e,1):
            res+=comb(n-1,k-1,exact=True)*f
        if res==0:
            print(res)
            continue
        ret=(sum(map(int,list(str(res)))))
        if ret%9:
            print(ret%9)
        else:
            print(9)