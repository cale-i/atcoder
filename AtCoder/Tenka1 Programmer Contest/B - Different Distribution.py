# 2019/12/18

n=int(input())
ab=[]
for i in range(n):
    a,b=map(int,input().split())
    ab.append((a,b))
ab.sort()
print(ab[-1][0]+ab[-1][1])