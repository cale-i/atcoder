n=int(input())
p=list(map(int,input().split()))

cnt=0
for i in range(1,n+1):
    if p[i-1]==i:continue
    cnt+=1
print('YES' if cnt<=2 else 'NO' )
