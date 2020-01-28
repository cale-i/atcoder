# yukicoder No.512 魔法少女の追いかけっこ 2020/01/28
# 丸め誤差回避=>除算を乗算にする

x,y=map(int,input().split())
n=int(input())
a=list(map(int,input().split()))

for i in range(n-1):
    dy=a[i]*y #a[i]*y/x(丸め誤差によりWAとなる場合がある)
    
    if dy>a[i+1]*x:
        print('NO')
        exit()
else:
    print('YES')