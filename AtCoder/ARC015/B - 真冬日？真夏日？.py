# 2019/12/1

n=int(input())
day=[0]*6 # 猛暑日・真夏日・夏日・熱帯夜・冬日・真冬日

for i in range(n):
    M,m=map(float,input().split())
    if M>=35:
        day[0]+=1
    elif M>=30:
        day[1]+=1
    elif M>=25:
        day[2]+=1
    if m>=25:
        day[3]+=1
    if M>=0 and m<0:
        day[4]+=1
    if M<0:
        day[5]+=1
print(*day)