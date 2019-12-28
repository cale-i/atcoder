# 2019/12/28

n,a,b=map(int,input().split())
if a%2==b%2:
    print((b-a)//2)
else:
    left=a-1
    right=n-b
    if left<right:
        b-=1
        print(a-1+(b-a)//2+1)
    else:
        a+=1
        print(n-b+(b-a)//2+1)