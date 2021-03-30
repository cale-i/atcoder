# 2019/12/28

a,b=map(int,input().split())
for i in range(a,b+1):
    if i%3 and str(i).count('3')==0:continue
    print(i)