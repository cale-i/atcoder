# yukicoder No.779 Heisei 2020/01/22

from datetime import datetime

y,m,d=map(int,input().split())

d=datetime(y,m,d)
bgn=datetime(1989,1,8)
end=datetime(2019,4,30)
if bgn<=d<=end:
    print('Yes')
else:
    print('No')
