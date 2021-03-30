# yukicoder No.682 Average 2020/01/25

a,b=map(int,input().split())
cnt=0
for i in range(a,b+1):
    d,m=divmod((a+b+i),3)
    if m==0:
        cnt+=1
print(cnt)