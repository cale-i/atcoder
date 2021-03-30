n=int(input())
p=list(map(int,input().split()))

lowest=10**9
cnt=0
for i in range(n):
    if p[i]<lowest:
        cnt+=1
        lowest=min(lowest,p[i])
print(cnt)