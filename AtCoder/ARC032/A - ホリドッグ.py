# 2019/10/12

n=int(input())
if n==1:
    print('BOWWOW')
    exit()
cnt=0
for i in range(1,n+1):
    cnt+=i
for i in range(2,int(pow(cnt,0.5)+1)):
    if cnt%i==0:
        print('BOWWOW')
        exit()
else:print('WANWAN')
