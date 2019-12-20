# 2019/12/20

h,w=map(int,input().split())
snuke=[list(input().split()) for _ in range(h)]

for i in range(h):
    for j in range(w):
        if snuke[i][j]!='snuke':continue
        print(chr(j+65)+str(i+1))
        exit()