# 2019/08/07
# かんにんぐ

n=int(input())
a=[0]+list(map(int,input().split()))+[0]

s=[]
for i in range(n+1):
    s.append(abs(a[i]-a[i+1]))
S=sum(s)
for i in range(1,n+1):
    ans=S+abs(a[i-1]-a[i+1])-(abs(a[i-1]-a[i])+abs(a[i]-a[i+1]))
    print(ans)
