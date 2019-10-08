# 2019/09/13

import datetime

y,m,d=map(int,input().split('/'))
dt=datetime.datetime(y,m,d)

while True:
    yy,mm,dd=dt.strftime('%F').split('-')
    if int(yy)%(int(mm)*int(dd))==0:
        print(yy,mm,dd,sep='/')
        break
    dt+=datetime.timedelta(days=1)



# 1個WAだった
# 理由わかんない
"""
y,m,d=map(int,input().split('/'))
days=[0,31,28,31,30,31,30,31,31,30,31,30,31]


def is_leap_year(y):
    ans=False
    if y%400==0:
        ans=True
    elif y%100:
        if y%4==0:
            ans=True
    return ans


if is_leap_year(y):
    days[2]=29


def solve(m,d):
    md=int(str(m)+str(d).zfill(2))
    for i in range(m,13):
        for j in range(1,days[i]+1):
            mmdd=int(str(i)+str(j).zfill(2))
            if mmdd<md:continue
            if y%(i*j):continue
            return y,i,j
    return y+1,1,1


Y,M,D=solve(m,d)

M=str(M).zfill(2)
D=str(D).zfill(2)
print(Y,M,D,sep='/')"""