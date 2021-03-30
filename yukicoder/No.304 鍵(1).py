# yukicoder No.304 鍵(1) 2020/02/02

for i in range(10):
    for j in range(10):
        for k in range(10):
            print(str(i)+str(j)+str(k))
            res=input()
            if res=='unlocked':
                exit()