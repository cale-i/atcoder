# 2019/08/12

n=int(input())
n-=1
c=[0]*n
s=[0]*n
f=[0]*n

for i in range(n):
    c[i],s[i],f[i]=map(int,input().split())

ans=[]
for i in range(n):
    res=c[i]+s[i]
    for j in range(i+1,n):
        if res<s[j]:
            res=s[j]+c[j]
        else:
            if res%f[j]:
                res+=f[j]-res%f[j]+c[j]
            else:
                res+=c[j]
    ans.append(res)
print(*ans,sep='\n')
print(0)