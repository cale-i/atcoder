# 2019/08/17
s=list(input())
cnt=0
pre=''
while s:
    tmp=s.pop()
    while s and pre==tmp:
        tmp=s.pop()+tmp
    if pre==tmp:continue
    else:
        pre=tmp
        cnt+=1
print(cnt)