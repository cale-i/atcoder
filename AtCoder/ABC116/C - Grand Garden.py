# 2019/08/09

n=int(input())
h=[0]+list(map(int,input().split()))+[0]
n+=2
cnt=0
btm=0
for i in range(n-1):
    if h[i]==h[i+1]:continue
    
    if h[i]<h[i+1]:
        btm=min(h[i],btm)
    else:
        cnt+=h[i]-btm
        btm=h[i+1]
print(cnt)