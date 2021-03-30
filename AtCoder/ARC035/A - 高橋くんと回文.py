# 2019/11/15

s=list(input())
ss=s[::-1]
for x,y in zip(s,ss):
    if x==y or x=='*' or y=='*':continue
    else:
        print('NO')
        exit()
else:print('YES')