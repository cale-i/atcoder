# 2019/11/18

h,w=map(int,input().split())

g=[list('@'*(w+2))]
for i in range(h):
    g+=[list('@')+list(map(int,input().split()))+list('@')]
g+=[list('@'*(w+2))]

dir=[(0,1),(1,0)]

n=0
ans=[]
for i in range(1,h+1):
    for j in range(1,w+1):
        if g[i][j]%2==0:
            continue
        right=g[i][j+1]
        down=g[i+1][j]            
        if right!='@':
            g[i][j]-=1
            g[i][j+1]+=1
            ans.append((i,j,i,j+1))
        elif down!='@':
            g[i][j]-=1
            g[i+1][j]+=1
            ans.append((i,j,i+1,j))
        else:continue
        n+=1
print(n)
[print(*e) for e in ans]