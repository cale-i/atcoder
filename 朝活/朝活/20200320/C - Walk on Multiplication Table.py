# https://atcoder.jp/contests/abc144/tasks/abc144_c

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

ans=float('inf')
for e in div:
    ans=min(ans,(e+n//e)-2)
print(ans)