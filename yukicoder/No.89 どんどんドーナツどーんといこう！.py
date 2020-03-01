# yukicoder No.89 どんどんドーナツどーんといこう！ 2020/03/02
# パップス・ギュルダンの定理
# 断面積は((Rin-Rout)/2)^2*π、重心の回転距離は((Rin-Rout)/2)*2*π

import math
c=int(input())
rin,rout=map(int,input().split())
r=(rout-rin)/2

center=rin+r
ans=(math.pi*pow(r,2))*(center*2*math.pi)
print(ans*c)