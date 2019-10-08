# 2019/08/01
# だめだめ

n,m=map(int,input().split())

def divisors(n,m):
    div=[]
    end=int(pow(m,0.5))
    for i in range(1,end+1):
        if m%i==0:
            div.append(i)
            div.append(m//i)
    div.sort(reverse=True)
    return div

res=divisors(n,m)
for e in res:
    if m//n>=e:
        print(e)
        break
