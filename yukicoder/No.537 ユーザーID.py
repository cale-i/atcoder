# yukicoder No.537 ユーザーID 2020/01/28

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

div=divisors(n)

ans=set()
for d in div:
    ans.add(str(d)+str(n//d))
print(len(ans))