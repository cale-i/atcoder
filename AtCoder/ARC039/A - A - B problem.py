# 2019/11/7
import copy

a,b=input().split()
a,b=list(a),list(b)
ans=-10000
for i in range(3):
    tmp=a[i]
    a[i]='9'
    ans=max(ans,int(''.join(a))-int(''.join(b)))
    a[i]=tmp
for i in range(3):
    tmp=b[i]
    b[i]='1' if i<1 else '0'
    ans=max(ans,int(''.join(a))-int(''.join(b)))
    b[i]=tmp
print(ans)