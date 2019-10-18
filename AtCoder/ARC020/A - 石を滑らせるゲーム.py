# 2019/09/29

a,b=map(int,input().split())
a=abs(a)
b=abs(b)
if a<b:ans='Ant'
elif b<a:ans='Bug'
else:ans='Draw'
print(ans)