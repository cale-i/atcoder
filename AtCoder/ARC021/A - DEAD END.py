# 2019/10/26

g=[list('0'*6)]
for i in range(4):
    g+=[['0']+list(input().split())+['0']]
g+=[list('0'*6)]

dir=[(0,1),(1,0)]


def solve(c,r):
    for y,x in dir:
        if g[r][c]==g[r+y][c+x]:
            print('CONTINUE')
            exit()


for r in range(1,5):
    for c in range(1,5):
        solve(c,r)
else:print('GAMEOVER')
