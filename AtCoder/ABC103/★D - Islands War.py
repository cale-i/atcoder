# 2019/07/02
# 区間スケジューリング？
# そのうちもう一回解く

n,m=map(int,input().split())

ab=[]
for i in range(m):
    ab.append(tuple(map(int,input().split())))

ab.sort(key=lambda x: x[1])

pre=0
cnt=0
for i in range(m):
    if pre<=ab[i][0]:
        pre=ab[i][1]
        cnt+=1
    else:
        pre=min(pre,ab[i][1])
print(cnt)