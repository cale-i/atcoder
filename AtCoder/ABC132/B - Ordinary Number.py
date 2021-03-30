n=int(input())
p=list(map(int,input().split()))

cnt=0
for i in range(2,n):
    a=p[i-2]
    b=p[i-1]
    c=p[i]
    if a<b<c or c<b<a:
        cnt+=1

print(cnt)