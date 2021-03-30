# yukicoder No.994 ばらばらコイン 2020/03/10

n,k=map(int,input().split())

if n<k:
    print(-1)
else:
    print(k-1)