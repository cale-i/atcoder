h,w=map(int,input().split())
w+=2
a=[['.']*w]
for i in range(h):
    a+=[['.']+list(input())+['.']]

a+=[['.']*w]

g=(h-1,w-1)
cnt=0

def dfs(x,y):
    if (x,y)==g:return True
    else:
        if a[x][y]=='#':
            a[x][y]='@'
            d=dfs(x+1,y)
            r=dfs(x,y+1)
            if d==r==True:
                return False
        else:
            return False
    return True

ans=dfs(1,1)
print(ans)