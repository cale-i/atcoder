# 2019/09/25


n,m,a,b=map(int,input().split())
for i in range(m):
    if n<=a:
        n+=b
    n-=int(input())
    if n<0:
        print(i+1)
        exit()
print('complete')