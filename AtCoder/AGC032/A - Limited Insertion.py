# 2019/09/03
# かんにんぐ

n=int(input())
b=[-1]+list(map(int,input().split()))

ans=[]
while b:
    lb=len(b)
    if lb==1:break
    idx=0
    for i in range(lb):
        if i==b[i]:
            idx=i
    if idx:
        ans.append(idx)
        b.remove(idx)
    else:
        print(-1)
        exit()

print(*ans[::-1],sep='\n')
