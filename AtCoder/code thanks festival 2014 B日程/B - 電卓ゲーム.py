# 2019/07/11

a=int(input())
b=int(input())
c=int(input())

ans=0
if a in [0,1] or b in [0,1]:ans+=a+b
else:ans+=a*b

if c in [0,1] or ans in [0,1]:
    ans+=c
else:ans*=c
print(ans)

# #3566393をみて

a=int(input())
b=int(input())
c=int(input())
res=max(a+b,a*b)
print(max(res+c,res*c))