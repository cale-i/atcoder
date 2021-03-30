# https://atcoder.jp/contests/abc134/tasks/abc134_d

n=int(input())
a=list(map(int,input().split()))


def divisors(n):
    div=[]
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            div.append(i)
            if i!=n//i:
                div.append(n//i)
    return div


for i in reversed(range(n)):
    div=divisors(i+1)
    