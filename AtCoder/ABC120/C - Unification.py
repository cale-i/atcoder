# 2019/07/25

s=input()

cnt=0
for e in s:
    if e=='1':cnt+=1
    else:cnt-=1
print(len(s)-abs(cnt))

# 別解

s=input()
z=s.count('0')
o=s.count('1')
print(len(s)-abs(z-o))