# 2019/12/29

a,b,k=map(int,input().split())

if a>=k:
    a-=k
else:
    a,b=0,max(b-(k-a),0)
print(a,b,sep=' ')