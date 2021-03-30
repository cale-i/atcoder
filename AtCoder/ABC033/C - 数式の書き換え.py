# 2019/08/26
 
s=input().split('+')

cnt=0
for e in s:
    if '0' not in e:
        cnt+=1
print(cnt)