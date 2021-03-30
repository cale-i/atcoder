# 2019/09/12

y=int(input())
ans='NO'
if y%400==0:
    ans='YES'
elif y%100:
    if y%4==0:
        ans='YES'
print(ans)

