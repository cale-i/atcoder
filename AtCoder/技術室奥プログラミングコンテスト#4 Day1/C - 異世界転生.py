# 2019/07/28

n,x=map(int,input().split())

for i in range(2,11):
    t=n
    res=[]
    while t:
        res.append(str(t%i))
        t//=i
    r=int(''.join(res[::-1]))
    if r==x:
        print(i)
        exit()

# int の楽しい使い方

n,x=map(int,input().split())

for i in range(2,11):
    try:
        res=int(str(x),i)
        if res==n:
            print(i)
            exit()
    except:
        pass