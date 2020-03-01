# yukicoder  No.98 円を描こう 2020/03/01

xp,yp=map(int,input().split())

rp=pow(xp**2+yp**2,1/2)
print(int(rp*2)+1)