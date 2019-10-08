# 2019/07/23

n,m=map(int,input().split())
a=sorted(list(map(int,input().split())),reverse=True)

i=0
cnt=0
res=0
while cnt<m:
    if cnt<m:
        cnt+=a[i]
        res+=1
        i+=1
print(res)