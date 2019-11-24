n=int(input())
a=list(map(int,input().split()))
SUM=sum(a)
hlf=SUM//2
cnt=0
res=float('inf')
for i in range(n):
    cnt+=a[i]
    rst=SUM-cnt
    if cnt==hlf:
        print(0)
        exit()
    res=min(abs(rst-cnt),res)
print(res)