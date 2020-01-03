# 2020/01/03
# バグらせすぎた

a=[int(input()) for _ in range(5)]

fib=[0,1]
num=0
while num<=max(a):
    num=fib[-1]+fib[-2]
    fib.append(num)
bgn=1
flag=False
if a[-1]==1:
    if a[-2]!=1:
        bgn=2
    else:
        bgn=1
        flag=True

cnt=0
e=a.pop()
for i in range(bgn,len(fib)):
    if flag:
        if fib[i]!=e:break
    else:
        if e!=fib[i]:continue
        flag=True
    cnt+=1
    if not a:break
    e=a.pop()
print(cnt)