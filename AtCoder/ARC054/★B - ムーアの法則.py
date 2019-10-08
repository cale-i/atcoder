# 2019/09/05
# わからん
p=float(input())
ans=[]
for i in range(100):
    s=2**(i/1.5)
    print(s)
    print('-------------')
    print(f'p/xは{p/s}です')
    print('-------------')
    ans.append(i+p/s)

for e in ans:
    print(e)
print(min(ans))