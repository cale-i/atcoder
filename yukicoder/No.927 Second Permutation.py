# 2020/01/17

x=sorted(list(input()),reverse=True)
n=len(x)
for i in reversed(range(1,n)):
    if x[i-1]==x[i]:continue
    x[i],x[i-1]=x[i-1],x[i]
    break
else:
    print(-1)    
    exit()

ans=int(''.join(x))
if len(str(ans))==len(x):
    print(ans)
else:print(-1)