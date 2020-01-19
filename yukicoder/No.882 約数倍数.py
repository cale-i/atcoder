# yukicoder No.882 約数倍数 2020/01/19

a,b=map(int,input().split())

def divisors(n):
    div=[]
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            div.append(i)
            if i!=n//i:
                div.append(n//i)
    div.sort()
    return div

div=divisors(a)

ans='YES'
for d in div:
    if d%b==0:break
else:
    ans='NO'
print(ans)