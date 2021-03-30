# 201907/24

n=int(input())
res=2025-n

ans=[]
for i in range(1,10):
    if res%i==0 and 1<=res//i<=9:
        ans.append((i,res//i))

for a,b in ans:
    print('{} x {}'.format(a,b))
