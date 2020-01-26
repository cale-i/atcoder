h,n=map(int,input().split())

ab=[tuple(map(int,input().split())) for _  in range(n)]
for i in range(n):
    for j in range(n):
        ab.append((ab[i][0]+ab[j][0],ab[i][1]+ab[j][1]))


ab.sort(key=lambda x: -(x[0]/x[1]))
print(ab)