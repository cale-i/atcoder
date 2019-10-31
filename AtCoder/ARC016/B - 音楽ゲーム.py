# 2019/10/31

n=int(input())
x=[]
for i in range(n):
    x.append(list(input()))
x.append(list('.........'))
cnt=0
for j in range(9):
    for i in range(n):
        xx=x[i][j]
        if xx=='.':continue
        if xx=='x':cnt+=1        
        else:
            if x[i+1][j]!='o':
                cnt+=1
print(cnt)