# 2019/10/29

n=int(input())

for i in range(1,10):
    for j in range(1,10):
        if n==i*j:
            print('Yes')
            exit()
else:
    print('No')