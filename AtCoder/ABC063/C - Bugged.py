# 2019/08/08

n=int(input())
s=sorted([int(input()) for _ in range(n)])

sum_s=sum(s)
if sum_s%10:
    print(sum_s)
    exit()

for i in range(n):
    if s[i]%10:
        print(sum_s-s[i])
        exit()
print(0)