# https://atcoder.jp/contests/arc010/tasks/arc010_1

n,m,a,b=map(int,input().split())
c=[int(input()) for _ in range(m)]

for i in range(m):
    if n<=a:
        n+=b
    if n<c[i]:
        print(i+1)
        break
    n-=c[i]
else:
    print('complete')