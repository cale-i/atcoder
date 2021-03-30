# yukicoder No.571 3人兄弟（その２） 2020/01/27

ls=['A','B','C']
hw=[list(map(int,input().split()))+[i] for i in range(3)]
hw.sort(key=lambda x: (-x[0],x[1]))
[print(ls[e[2]]) for e in hw]