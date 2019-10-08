# 2019/09/01
s=input()
t=input()

cnt=0
for a,b in zip(s,t):
    if a==b:
        cnt+=1

print(cnt)