# yukicoder No.888 約数の総和 2020/01/19

n=int(input())

def divisors(n):
    div=[]
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            div.append(i)
            if i!=n//i:
                div.append(n//i)
    div.sort()
    return div

print(sum(divisors(n)))