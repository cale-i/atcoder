# 2019/112/28

n,m,v,p=map(int,input().split())
a=sorted(map(int,input().split()),reverse=True)
c=0
border=a[p-1]
for i in range(p,n):
    if a[i]==border:
        p+=1
    else:
        if a[i]+m>=border:
            c+=1
        a[i]+=m
        v-=1

drop=a.count(border)
if p-drop>=v:
    p+=min(c,drop)
else:
    

print(p)
    