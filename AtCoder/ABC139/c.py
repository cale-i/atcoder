# 2019/09/01

n=int(input())
h=list(map(int,input().split()))[::-1]

cnt=0
ans=[]
for i in range(n-1):
    if h[i]<=h[i+1]:
        cnt+=1
        ans.append(cnt)    
    else:
        cnt=0
if ans:
    print(max(ans))
else:
    print(0)