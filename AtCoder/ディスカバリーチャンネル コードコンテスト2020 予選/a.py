x,y=map(int,input().split())


def solve(x):
    ret=0
    if x==1:
        ret+=300000
    elif x==2:
        ret+=200000
    elif x==3:
        ret+=100000
    return ret

ans=0

ans+=solve(x)+solve(y)
if x==y==1:
    ans+=400000
print(ans)