h,w=map(int,input().split())
s=[['a']*(w+2)] +  [['a']+list(input())+['a'] for i in range(h)] +[['a']*(w+2)]

dx=[-1,0,1,-1,1,-1,0,1]
dy=[-1,-1,-1,0,0,1,1,1]

for i in range(h+1):
    for j in range(w+1):
        c=''
        if s[i][j]!='#':
            for x,y in zip(dx,dy):
                c+=s[i+x][j+y]
            s[i][j]=str(c.count('#'))
for i in range(1,h+1):
    print(''.join(s[i][1:-1]))
