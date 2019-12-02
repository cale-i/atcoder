# 2019/12/1

n=int(input())
for i in range(50000):
    if int(i*1.08)==n:
        print(i)
        exit()
else:
    print(':(')