# yukicoder No.231 めぐるはめぐる (1) 2020/02/03

n=int(input())
gd=[]
for i in range(n):
    g,d=map(int,input().split())
    gd.append((g-d*30000,i+1))

gd.sort()
if gd[-1][0]*6>=3*10**6:
    print('YES')
    [print(gd[-1][1]) for _ in range(6)]
else:
    print('NO')