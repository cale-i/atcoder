# 2019/08/09

n=int(input())
acc=[0]
for i in range(1,n+1):
    acc.append(i+acc[i-1])
    if acc[i]==n:
        print(*range(1,i+1),sep='\n')
        exit()
    elif acc[i]>n:
        idx=i
        break

rem=acc[idx]-n
for i in range(1,idx+1):
    if i!=rem:
        print(i)
