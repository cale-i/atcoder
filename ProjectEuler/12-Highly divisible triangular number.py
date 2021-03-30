# 2019/12/10

def divisors(n):
    div=0
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            div+=1
            if i!=n//i:
                div+=1
    return div

div=0
n=500
tri=0
i=0
while div<n:
    i+=1
    tri+=i
    div=divisors(tri)
print(tri)