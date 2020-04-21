# https://atcoder.jp/contests/abc088/tasks/abc088_c

c=[list(map(int,input().split())) for _ in range(3)]

for i in range(2):
    res1=c[i+1][0]-c[i][0]
    res2=c[i+1][1]-c[i][1]
    res3=c[i+1][2]-c[i][2]
    if res1==res2==res3:continue
    else:
        print('No')
        exit()


for j in range(2):
    res1=c[0][j+1]-c[0][j]
    res2=c[1][j+1]-c[1][j]
    res3=c[2][j+1]-c[2][j]
    if res1==res2==res3:continue
    else:
        print('No')
        exit()

print('Yes')