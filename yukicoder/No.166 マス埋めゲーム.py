# yukicoder No.166 マス埋めゲーム 2020/02/04

h,w,n,k=map(int,input().split())

hw=h*w
if n==1 :
    print('YES')
    exit()
if hw%n==k%n:
    print('YES')
else:
    print('NO')