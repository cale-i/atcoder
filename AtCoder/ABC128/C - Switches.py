# 2019/09/22

n,m=map(int,input().split())
s=[]
for i in range(m):
    _,*ss=map(lambda x:int(x)-1,input().split())
    
    s.append(ss)
p=list(map(int,input().split()))

res=0
for i in range(2**n):
    flag=True
    for j in range(m):
        cnt=0
        for e in s[j]:
            if i>>e&1:
                cnt+=1

        if cnt%2!=p[j]:
            flag=False
            break
    if flag:res+=1
print(res)