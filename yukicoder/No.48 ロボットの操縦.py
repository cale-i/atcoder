# 2019/12/28

x=int(input())
y=int(input())
l=int(input())
ans=0

if y>=0 and x!=0:ans+=1
elif y<0:ans+=2

ans+=(-(-abs(y)//l)+-(-abs(x)//l))
print(ans)