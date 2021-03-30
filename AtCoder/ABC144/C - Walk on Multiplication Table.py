# 2019/10/29
# 14min

def divisors(n):
    div=[]
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            div.append(i)
    div.sort()
    return div


n=int(input())
div=divisors(n)
res=float('inf')
for e in div:
    d=e+n//e-2
    res=min(res,d)
print(res)