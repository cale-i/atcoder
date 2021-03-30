# 2019/10/07
import datetime

y,m,d=[input() for _ in range(3)]
y=y.zfill(4)
pd=datetime.datetime.strptime(y+m+d,'%Y%m%d')
nd=datetime.datetime.strptime('20140517','%Y%m%d')
ans=(nd-pd).days
print(ans)