# 2019/12/28

import datetime
sy=2015
sm=1
sd=1

ey=2016
em=1
ed=1

date=datetime.date(sy,sm,sd)
end=datetime.date(ey,em,ed)
td=datetime.timedelta(days=1)

ans=0
while date!=end:
    month=date.month
    day=date.day
    if month==sum(map(int,list(str(day)))):
        ans+=1
    date+=td
print(ans)