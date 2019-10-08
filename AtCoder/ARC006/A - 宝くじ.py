# 2019/09/13

e=list(map(int,input().split()))
b=int(input())
l=list(map(int,input().split()))

cnt=0
flag=False
for ll in l:
    if ll in e:
        cnt+=1
    if ll==b:
        flag=True

if cnt==6:
    ans=1
elif cnt==5 :
    if flag:ans=2
    else:ans=3
elif cnt==4:
    ans=4
elif cnt==3:
    ans=5
else:ans=0
print(ans)