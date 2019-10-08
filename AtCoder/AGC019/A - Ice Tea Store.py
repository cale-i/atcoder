# 2019/08/08

Q,H,S,D=map(int,input().split())
n=int(input())

q=Q*4
h=H*2
s=S
d=D/2
ls=sorted([q,h,s,d])
if ls[0]==d and ls[1]!=d:
    if n%2:
        ans=D*(n//2)+ls[1]
    else:
        ans=D*(n//2)

else:
    ans=int(ls[0]*n)
print(ans)

# 回答のやつ
# 2019/08/08

Q,H,S,D=map(int,input().split())
n=int(input())

ans=(n//2)*min(8*Q,4*H,2*S,D)+(n%2)*(min(4*Q,2*H,S))
print(ans)