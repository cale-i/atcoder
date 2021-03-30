# 2019/10/06

S=input().lower()
i=-1 
for e in 'ict':
    while i+1<len(S):
        i+=1
        if e==S[i]:break
    else:
        print('NO')
        exit()
print('YES')