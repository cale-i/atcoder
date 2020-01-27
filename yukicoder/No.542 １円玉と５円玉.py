# yukicoder No.542 １円玉と５円玉 2020/01/27

a,b=map(int,input().split())

ans=set()
for i in range(a+1):
    for j in range(b+1):
        if i==j==0:continue
        ans.add(i+j*5)
ans=sorted(ans)
print(*ans,sep='\n')